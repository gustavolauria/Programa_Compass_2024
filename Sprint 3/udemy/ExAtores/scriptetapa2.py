soma = 0
contagem = 0


with open('arquivo_limpo.txt', 'r', encoding='utf-8') as file:
    
    linhas = file.readlines()


for linha in linhas:
    
    colunas = linha.strip().split(',')
    
    valor_coluna = float(colunas[5])
    
    soma += valor_coluna
    contagem += 1


media = soma / contagem

with open('etapa2.txt', 'w', encoding='utf-8') as file:
    file.write(f"A média da sexta coluna é: {media}")
   