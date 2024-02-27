with open('arquivo_limpo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

atores_bilheteria = []

for linha in linhas[0:]:  
    dados = linha.strip().split(',')
    ator = dados[0]
    bilheteria = float(dados[1])
    atores_bilheteria.append((ator, bilheteria))

atores_bilheteria.sort(key=lambda x: x[1], reverse=True)

with open('etapa5.txt', 'w') as arquivo_saida:
    for ator, bilheteria in atores_bilheteria:
        arquivo_saida.write(f"{ator} - {bilheteria}\n")