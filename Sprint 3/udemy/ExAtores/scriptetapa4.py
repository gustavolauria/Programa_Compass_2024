ocorrencias_filmes = {}

with open('arquivo_limpo.txt', 'r') as file:
    
    for linha in file:
        colunas = linha.split(',')

        nome_filme = colunas[4].strip() 

        if nome_filme in ocorrencias_filmes:
            ocorrencias_filmes[nome_filme] += 1
        else:
            ocorrencias_filmes[nome_filme] = 1

ocorrencias_filmes_ordenado = dict(sorted(ocorrencias_filmes.items(), key=lambda item: (-item[1], item[0])))


with open('etapa4.txt', 'w') as arquivo:
    
    for filme, ocorrencias in ocorrencias_filmes_ordenado.items():
        arquivo.write("O filme {} aparece {} vez(es) no dataset\n".format(filme, ocorrencias))