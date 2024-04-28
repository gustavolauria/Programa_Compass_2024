import requests
import boto3
import json
import os
from datetime import datetime
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

def obter_valores_distintos_com_filtro(caminho_arquivo, delimiter=';', encoding='latin-1', keywords=['Sci-Fi', 'Fantasy']):
    try:
        df = pd.read_csv(caminho_arquivo, delimiter=delimiter, encoding=encoding, skiprows=1)
        coluna_generos = df.iloc[:, 5]  
        coluna_valores = df.iloc[:, 7]  
        
        ids_filtrados = set()  
        
        for index, (generos, valor) in enumerate(zip(coluna_generos, coluna_valores)):
            if any(keyword in generos for keyword in keywords) and valor > 1000:
                movie_id = df.iloc[index, 0]  
                ids_filtrados.add(movie_id)

        return list(ids_filtrados)

    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return []

def obter_dados_filme(movie_id, headers):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=headers)
    movie_data = response.json()
    
    
    if movie_data.get('budget', 0) > 0 and movie_data.get('revenue', 0) > 0:
        return movie_data
    else:
        return None  

def obter_dados_filmes_em_lotes(valores_distintos, headers, tamanho_lote, pasta_saida):
    with ThreadPoolExecutor() as executor:
        resultados = []
        
        for i in range(0, len(valores_distintos), tamanho_lote):
            lote_ids = valores_distintos[i:i + tamanho_lote]
            lote_dados = []
            
            for movie_id in lote_ids:
                futures = executor.submit(obter_dados_filme, movie_id, headers)
                resultados.append(futures)
        
       
        lote_index = 0
        for idx, future in enumerate(as_completed(resultados)):
            movie_data = future.result()
            if movie_data is not None:
                lote_dados.append(movie_data)
            
            
            if len(lote_dados) == tamanho_lote or (idx == len(resultados) - 1):
                if len(lote_dados) > 0:  
                    nome_arquivo_saida = f"{pasta_saida}filmes_{lote_index}.json"
                    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
                        json.dump(lote_dados, arquivo_saida)
                    lote_index += 1
                    lote_dados = []  
        
    print("Processo concluído!")

def upload_file_to_s3(file_path, bucket_name, s3_key):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"Arquivo {file_path} enviado com sucesso para o S3!")
    except Exception as e:
        print(f"Erro ao enviar arquivo para o S3: {e}")

   
bucket_name = 'data-lake-desafio-final'
s3_base_folder = 'Raw/TMDB/JSON'


today = datetime.now()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')

pasta_local = 'respostas_api/'

caminho_para_csv = 'movies.csv'

valores_distintos = obter_valores_distintos_com_filtro(caminho_para_csv)

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZjRmYjY0NDk4NTQwMDBmZmI0OTUxZTAzNGM0NDgwNSIsInN1YiI6IjY2MjE5OTMyZTY0MGQ2MDE4NmMzOTBjOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.d2iH6DG4awALsAMqF7L_zSpQUy2Tdhc8CZK7VNhPMzI"
}

pasta_saida = 'respostas_api/'

tamanho_lote = 100

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

obter_dados_filmes_em_lotes(valores_distintos, headers, tamanho_lote, pasta_saida)

for i in range(14):
    filename = f'filmes_{i}.json' 
    filmes_path = f'respostas_api/{filename}'
    s3_key = f"{s3_base_folder}/{year}/{month}/{day}/{filename}"
    upload_file_to_s3(filmes_path, bucket_name, s3_key)

print("Processo concluído!")
