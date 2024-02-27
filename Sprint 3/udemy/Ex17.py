#Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
#a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def divide_lista(lista):
    tamanho_parte = len(lista) // 3
    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte: tamanho_parte * 2]
    parte3 = lista[tamanho_parte * 2:]
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

parte1, parte2, parte3 = divide_lista(lista)

print(parte1,parte2,parte3)
