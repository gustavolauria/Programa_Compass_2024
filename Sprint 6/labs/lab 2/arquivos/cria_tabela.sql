CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.tb_nomes (
     Nome STRING, 
     Sexo STRING, 
     Total INT, 
     Ano INT ) 
     ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
     WITH SERDEPROPERTIES ( 
        'serialization.format' = ',', 'field.delim' = ',' ) 
     LOCATION 's3://bucket.lab.aws.s3/dados/'