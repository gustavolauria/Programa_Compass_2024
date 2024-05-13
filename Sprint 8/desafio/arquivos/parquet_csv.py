import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import when


args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH','S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
output_path = args['S3_OUTPUT_PATH']

schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPrincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", IntegerType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", StringType(), True),
    StructField("anoFalecimento", StringType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

df = spark.read.csv(source_file, header=True, schema=schema, sep="|")

colunas_excluir = ["generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos"]
df = df.drop(*colunas_excluir)

df_novo = df.dropDuplicates(subset=["id"])

df_novo.write.parquet(output_path)
df_novo.show()
job.commit()