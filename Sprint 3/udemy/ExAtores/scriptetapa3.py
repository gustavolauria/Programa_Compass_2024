with open('arquivo_limpo.txt', 'r') as file:
    
    maior_média_bruta = 0
    nome_maior_média_bruta = ""

    
    for linha in file:
        
        colunas = linha.split(',')

        nome_ator = colunas[0]
        média_bruta = float(colunas[3])

        
        if média_bruta > maior_média_bruta:
            maior_média_bruta = média_bruta
            nome_maior_média_bruta = nome_ator.strip()  

with open('etapa3.txt', 'w') as file:
    file.write("O ator com a maior media bruta e: {} com a media de: {}\n".format(nome_maior_média_bruta, maior_média_bruta))