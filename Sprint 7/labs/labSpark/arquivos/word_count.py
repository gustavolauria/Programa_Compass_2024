from pyspark.sql import functions as F

df = spark.read.text("README.md?token=replace")

word_counts = df.select(F.explode(F.split(df.value, "\s+")).alias("word")).withColumn("word", F.lower(F.col("word"))).groupBy("word").count().orderBy("word")

word_counts.show(word_counts.count(), truncate=False)
