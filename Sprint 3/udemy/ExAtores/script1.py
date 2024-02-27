
with open('actors.csv', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

linhas = linhas[1:]

linhas_limpa = []


for linha in linhas:
    
    colunas = linha.strip().split(',')
    
    if colunas[0][0] == '"':
        colunas[0] = colunas[0][1:]
    
    if 'Robert Downey' in colunas[0]:
        colunas[0] += ' Jr.'
        del colunas[1]

    linhas_limpa.append(','.join(colunas))


with open('arquivo_limpo.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(linhas_limpa))

print("Arquivo limpo foi salvo como 'arquivo_limpo.txt'.")