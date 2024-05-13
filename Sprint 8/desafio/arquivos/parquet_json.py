import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


source_folder = args['S3_INPUT_PATH']
output_folder = args['S3_OUTPUT_PATH']

file_paths = []

for i in range(0, 1301, 100):
    file_name = f"filmes_{i}.json"
    file_paths.append(f"{source_folder}/{file_name}")
df = spark.read.json(file_paths)

colunas_excluir = ["adult", "backdrop_path", "belongs_to_collection", "homepage", "overview",
                   "poster_path", "production_companies", "production_countries", "spoken_languages",
                   "status", "tagline", "video"]

df = df.drop(*colunas_excluir)
df.show()

df_with_profits = df.withColumn('profits', col('revenue') - col('budget'))
df_with_profits.show()

df_with_profits.write.parquet(output_folder)

job.commit()