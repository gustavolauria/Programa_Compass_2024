import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, desc

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_OUTPUT_PATH']

input_df = spark.read.csv(source_file, header=True, inferSchema=True)

print("Esquema do DataFrame:")
input_df.printSchema()

print("Algumas linhas do DataFrame original:")
input_df.show(5, truncate=False)

#MAIUSCULA
input_df = input_df.withColumn(input_df.columns[0], upper(col(input_df.columns[0])))

print("Primeiras 5 linhas do DataFrame após a modificação:")
input_df.show(5, truncate=False)

input_df.write.partitionBy("sexo", "ano").json(target_path)

print("Contagem de linhas no DataFrame:")
print(input_df.count())

contagem_nomes = input_df.groupBy("ano", "sexo").count().orderBy(col("ano").desc())

print("Contagem de nomes por ano e sexo (ordenado pelo ano mais recente primeiro):")
contagem_nomes.show(truncate=False)

input_df_feminino = input_df.filter(input_df["sexo"] == "F")
registro_feminino_mais_frequente = input_df_feminino.orderBy(desc("total")).first()
nome_feminino_mais_registros = registro_feminino_mais_frequente["nome"]
ano_max_registros = registro_feminino_mais_frequente["ano"]

print(f"Nome: '{nome_feminino_mais_registros}' Ano: {ano_max_registros}.")

input_df_masculino = input_df.filter(input_df["sexo"] == "M")
registro_masculino_mais_frequente = input_df_masculino.orderBy(desc("total")).first()
nome_masculino_mais_registros = registro_masculino_mais_frequente["nome"]
ano_max_registros_masculino = registro_masculino_mais_frequente["ano"]

print(f"Nome: '{nome_masculino_mais_registros}' Ano: {ano_max_registros_masculino}.")

ano_total_df = input_df.select("ano", "total")

total_por_ano = (
    ano_total_df
    .groupBy("ano")
    .agg({"total": "sum"})
    .orderBy("ano")
)

print("Total de registros por ano:")
total_por_ano.show(10)

job.commit()