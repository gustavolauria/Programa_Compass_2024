import boto3
import os
from datetime import datetime

def upload_file_to_s3(file_path, bucket_name, s3_key):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"Arquivo {file_path} enviado com sucesso para o S3!")
    except Exception as e:
        print(f"Erro ao enviar arquivo para o S3: {e}")

   
bucket_name = 'data-lake-desafio-final'
s3_base_folder = 'Raw/Local/CSV'


today = datetime.now()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')

movies_csv_path = 'movies.csv'
s3_key = f"{s3_base_folder}/Movies/{year}/{month}/{day}/movies.csv"
upload_file_to_s3(movies_csv_path, bucket_name, s3_key)

series_csv_path = 'series.csv' 
s3_key = f"{s3_base_folder}/Series/{year}/{month}/{day}/series.csv"
upload_file_to_s3(series_csv_path, bucket_name, s3_key)
    
