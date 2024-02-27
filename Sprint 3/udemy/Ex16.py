#Escreva uma função que recebe uma string de números separados por vírgula 
#e retorne a soma de todos eles. Depois imprima a soma dos valores.
#A string deve ter valor  "1,3,4,6,10,76"


def soma_numeros(string_numeros):
    numeros = [int(numero) for numero in string_numeros.split(',')]

    soma = sum(numeros)

    return soma


string_numeros = "1,3,4,6,10,76"


print(soma_numeros(string_numeros))