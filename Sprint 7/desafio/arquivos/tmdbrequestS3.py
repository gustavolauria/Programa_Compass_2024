import json
import boto3
import os
from datetime import datetime
import pandas as pd
from urllib3 import PoolManager

def lambda_handler(event, context):
    def obter_valores_distintos_com_filtro(encoding='latin-1'):
        try:
            bucket_name = 'data-lake-desafio-final'
            s3_key = 'Raw/Local/CSV/Movies/2024/04/10/id.txt'
    
            s3_client = boto3.client('s3')
    
            response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
            
            file_content = response['Body'].read().decode(encoding)
            
            return file_content.splitlines()
    
        except Exception as e:
            print(f"Erro ao ler o arquivo txt do S3: {e}")
            return []

    def obter_dados_filme(movie_id, headers):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    
        http = PoolManager()
    
        try:
            response = http.request('GET', url, headers=headers)
    
            if response.status == 200:
                
                movie_data = json.loads(response.data.decode('utf-8'))
                
                if movie_data.get('budget', 0) > 0 and movie_data.get('revenue', 0) > 0:
                    return movie_data
                else:
                    return None
            else:
                print(f"Erro na requisição: {response.status}")
                return None
        except Exception as e:
            print(f"Erro ao obter os dados do filme {movie_id}: {e}")
            return None
    
    def obter_dados_filmes_em_lotes(valores_distintos, headers, tamanho_lote, s3_client, bucket_name, s3_base_folder, year, month, day):
        resultados = []
        lote_dados = []
        for movie_id in valores_distintos:
            movie_data = obter_dados_filme(movie_id, headers)
            if movie_data is not None:
                lote_dados.append(movie_data)
            if len(lote_dados) >= tamanho_lote:
                nome_arquivo_saida = f"{s3_base_folder}/{year}/{month}/{day}/filmes_{len(resultados)}.json"
                s3_key = f"{s3_base_folder}/{year}/{month}/{day}/filmes_{len(resultados)}.json"
                
                try:
                    s3_client.put_object(Body=json.dumps(lote_dados), Bucket=bucket_name, Key=s3_key)
                    print(f"Arquivo {nome_arquivo_saida} enviado com sucesso para o S3!")
                except Exception as e:
                    print(f"Erro ao enviar arquivo {nome_arquivo_saida} para o S3: {e}")
                
                resultados.extend(lote_dados)
                lote_dados = []
        
        if lote_dados:  
            nome_arquivo_saida = f"{s3_base_folder}/{year}/{month}/{day}/filmes_{len(resultados)}.json"
            s3_key = f"{s3_base_folder}/{year}/{month}/{day}/filmes_{len(resultados)}.json"
            
            try:
                s3_client.put_object(Body=json.dumps(lote_dados), Bucket=bucket_name, Key=s3_key)
                print(f"Arquivo {nome_arquivo_saida} enviado com sucesso para o S3!")
            except Exception as e:
                print(f"Erro ao enviar arquivo {nome_arquivo_saida} para o S3: {e}")
            
            resultados.extend(lote_dados)
        
        print("Processo obter_dados_filmes_em_lotes concluído!")
        return resultados
    
    bucket_name = 'data-lake-desafio-final'
    s3_base_folder = 'Raw/TMDB/JSON'
    
    today = datetime.now()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')
    
    valores_distintos = obter_valores_distintos_com_filtro()
    
    headers = os.environ.get("headers")
    
    tamanho_lote = 100
    
    s3_client = boto3.client('s3')
    
    resultados = obter_dados_filmes_em_lotes(valores_distintos, headers,tamanho_lote, s3_client, bucket_name, s3_base_folder, year, month, day)
    
    print("Processo Completo concluído!")
    return {
        'statusCode': 200
    }