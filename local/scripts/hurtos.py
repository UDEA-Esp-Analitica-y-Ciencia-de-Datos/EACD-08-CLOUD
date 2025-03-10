import sys
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession\
    .builder\
    .appName("SparkETL")\
    .getOrCreate()
   
data = spark.read.option("inferSchema", "true").option("header", "true").option("delimiter", ";").csv(sys.argv[1])
print('Columnas del dataset')
data.columns
print('1. Top 10 de los municipios de Antioquia que presentan mayor y menor número de hurtos')
mun=data.filter(data.DEPARTAMENTO=="ANTIOQUIA")
contmun=mun.groupBy("MUNICIPIO").count()
contmun.sort("count", ascending=False).show(10)
print('2.1. Tipos de armas más utilizadas en zona urbana')
urbana=data.filter(data.ZONA=="URBANA").groupBy("ARMA EMPLEADA").count().sort("count", ascending=False)
print(urbana.show())
rural=data.filter(data.ZONA=="RURAL").groupBy("ARMA EMPLEADA").count().sort("count", ascending=False)
print('2.2. Tipos de armas más utilizadas en zona rural')
print(rural.show())

print('Adiciono columna con fecha actual')
data = data.withColumn("FECHA ACTUAL", lit(datetime.now()))
print(data.show())
data.write.csv
data.write.csv(sys.argv[2])