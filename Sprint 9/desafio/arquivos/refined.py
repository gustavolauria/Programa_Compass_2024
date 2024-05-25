import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, upper, desc, explode, array,monotonically_increasing_id
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import regexp_replace, trim,split
from pyspark.sql.functions import year, month, dayofmonth
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_CSV', 'S3_INPUT_PATH_JSON', 'S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída
input_path1 = args['S3_INPUT_PATH_JSON']
input_path2 = args['S3_INPUT_PATH_CSV']
output_path = args['S3_OUTPUT_PATH']

file_paths1 = [
    f"{input_path1}/part-00000-03a6774a-d173-4a09-943e-43c1cf3685c2-c000.snappy.parquet",
    f"{input_path1}/part-00001-03a6774a-d173-4a09-943e-43c1cf3685c2-c000.snappy.parquet",
    f"{input_path1}/part-00002-03a6774a-d173-4a09-943e-43c1cf3685c2-c000.snappy.parquet",
    f"{input_path1}/part-00003-03a6774a-d173-4a09-943e-43c1cf3685c2-c000.snappy.parquet"
]
df1 = spark.read.parquet(*file_paths1)

file_paths2 = [
    f"{input_path2}/part-00000-2b661855-aedf-4f91-b8a3-d7d2f83a32a0-c000.snappy.parquet",
    f"{input_path2}/part-00001-2b661855-aedf-4f91-b8a3-d7d2f83a32a0-c000.snappy.parquet",
    f"{input_path2}/part-00002-2b661855-aedf-4f91-b8a3-d7d2f83a32a0-c000.snappy.parquet",
    f"{input_path2}/part-00003-2b661855-aedf-4f91-b8a3-d7d2f83a32a0-c000.snappy.parquet"
]
df2 = spark.read.parquet(*file_paths2)

joined_df = df1.join(df2, df1["imdb_id"] == df2["id"], "inner")

final_df = joined_df.select(
    col("imdb_id").alias("id_movie"),
    col("title"),
    col("release_date"),
    col("revenue"),
    col("budget"),
    col("profits"),
    col("genero").alias("genres"),
    col("popularity"),
    col("runtime"),
    col("vote_average"),
    col("vote_count")
)

final_df = final_df.withColumn("time_id", monotonically_increasing_id())
final_df = final_df.withColumn("sub_genre_id", monotonically_increasing_id())

final_df = final_df.withColumn("id_movie", regexp_replace(col("id_movie"), "^tt", ""))

final_df = final_df.withColumn("genres", regexp_replace(col("genres"), r"\bSci-Fi\b,?\s*|\bFantasy\b,?\s*", ""))
final_df = final_df.withColumn("genres", trim(regexp_replace(col("genres"), r",\s*$|^\s*,", "")))


dim_data = final_df.select(
    col("time_id").alias("Time_Id"),
    (year("release_date") - (year("release_date") % 10)).alias("Decade"),
    year("release_date").alias("Year"),
    month("release_date").alias("Month"),
    dayofmonth("release_date").alias("Day")
).distinct()

#dim_data = dim_data.orderBy("Time_Id")
dim_data.createOrReplaceTempView("Dim_Data")
#spark.sql("SELECT * FROM Dim_Data").show()

dim_sub_genre = final_df.select(
    col("sub_genre_id").alias("Sub-Genre_Id"),
    split(col("genres"), ",\s*").getItem(0).alias("Sub_Genre"),
    split(col("genres"), ",\s*").getItem(1).alias("Sub_Genre1")
)

dim_sub_genre.createOrReplaceTempView("Dim_Sub_Genre")
#spark.sql("SELECT * FROM Dim_Sub_Genre").show()

fato_movie = final_df.select(
    col("id_movie").alias("Movie_id"),
    col("time_id").alias("Time_Id"),
    col("sub_genre_id").alias("Sub_Genre_Id"),
    col("title").alias("Title"),
    col("runtime").alias("Runtime"),
    col("budget").alias("Budget"),
    col("revenue").alias("Revenue"),
    col("profits").alias("Profits"),
    col("popularity").alias("Popularity"),
    col("vote_average").alias("Vote_Average"),
    col("vote_count").alias("Vote_Count"),
).distinct()

#fato_movie = fato_movie.orderBy("Time_Id")
fato_movie.createOrReplaceTempView("Fato_Movie")
#spark.sql("SELECT * FROM Fato_Movie").show()

dim_data.write.mode("overwrite").parquet(f"{output_path}/dim_data")
dim_sub_genre.write.mode("overwrite").parquet(f"{output_path}/dim_sub_genre")
fato_movie.write.mode("overwrite").parquet(f"{output_path}/fato_movie")

job.commit()