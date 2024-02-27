soma = 0
contagem = 0


with open('arquivo_limpo.txt', 'r', encoding='utf-8') as file:
    
    linhas = file.readlines()

# Iterar pelas linhas do arquivo
for linha in linhas:
    # Dividir a linha em colunas
    colunas = linha.strip().split(',')
    # Extrair o valor da sexta coluna e converter para float
    valor_coluna = float(colunas[5])
    # Adicionar o valor à soma e incrementar a contagem
    soma += valor_coluna
    contagem += 1


media = soma / contagem

with open('etapa2.txt', 'w', encoding='utf-8') as file:
    file.write(f"A média da sexta coluna é: {media}")
   