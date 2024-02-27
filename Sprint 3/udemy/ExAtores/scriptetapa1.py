
max_filmes = 0
nome_max_filmes = ""

with open('arquivo_limpo.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

for linha in linhas:
   
    colunas = linha.strip().split(',')
    
    nome_ator = colunas[0]
    quantidade_filmes = int(colunas[2])
    
    if quantidade_filmes > max_filmes:
        max_filmes = quantidade_filmes
        nome_max_filmes = nome_ator


with open('etapa1.txt', 'w', encoding='utf-8') as file:
    file.write(f"O ator com o maior número de filmes é: {nome_max_filmes}\n")
    file.write(f"Ele atuou em um total de {max_filmes} filmes.")

print("Resultado salvo no arquivo 'etapa1.txt'.")