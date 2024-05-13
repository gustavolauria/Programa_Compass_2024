from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand
from pyspark.sql import functions as F

#ETAPA 1
spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes.show(5)

#ETAPA 2
df_nomes.printSchema()
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.printSchema()

df_nomes.show(10)
#ETAPA 3
df_nomes = df_nomes.withColumn("Escolaridade", F.when(rand() < 0.33, "Fundamental")
                               .when(rand() < 0.66, "Médio")
                               .otherwise("Superior"))

df_nomes.show(10)
#ETAPA 4
paises_americadosul = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador",
                        "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"]


df_nomes = df_nomes.withColumn("Pais", F.when(rand() < (1/13), paises_americadosul[0])
                                          .when(rand() < (2/13), paises_americadosul[1])
                                          .when(rand() < (3/13), paises_americadosul[2])
                                          .when(rand() < (4/13), paises_americadosul[3])
                                          .when(rand() < (5/13), paises_americadosul[4])
                                          .when(rand() < (6/13), paises_americadosul[5])
                                          .when(rand() < (7/13), paises_americadosul[6])
                                          .when(rand() < (8/13), paises_americadosul[7])
                                          .when(rand() < (9/13), paises_americadosul[8])
                                          .when(rand() < (10/13), paises_americadosul[9])
                                          .when(rand() < (11/13), paises_americadosul[10])
                                          .when(rand() < (12/13), paises_americadosul[11])
                                          .otherwise(paises_americadosul[12]))

df_nomes.show(10)
#ETAPA 5
df_nomes = df_nomes.withColumn("AnoNascimento", (F.rand() * (2010 - 1945) + 1945).cast("integer"))

df_nomes.show(10)
#ETAPA 6
df_select = df_nomes.filter(df_nomes.AnoNascimento >= 2001)

df_select.show(10)
#ETAPA 7
df_nomes.createOrReplaceTempView("pessoas")

query = """
    SELECT *
    FROM pessoas
    WHERE AnoNascimento >= 2001
"""

df_select_SQL = spark.sql(query)

df_select_SQL.show(10)
#ETAPA 8
num_pessoas = df_nomes.filter((df_nomes.AnoNascimento >= 1980) & (df_nomes.AnoNascimento <= 1994)).count()

print("Número de Millenials:", num_pessoas)
#ETAPA 9
query1 = """
    SELECT COUNT(*)
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
"""

resultado = spark.sql(query1)
num_pessoas = resultado.first()[0]

print("Número de Millenials:", num_pessoas)
#ETAPA 10
query2 = """
    SELECT
        CASE 
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            ELSE 'Geração Z'
        END AS Geracao,
        Pais,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Geracao, Pais
    ORDER BY Pais ASC, Geracao ASC
"""

df_geracoes = spark.sql(query2)

df_geracoes.show(n=False)