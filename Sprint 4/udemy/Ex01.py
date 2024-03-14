#Você está recebendo um arquivo contendo 10.000 números inteiros, 
#um em cada linha. Utilizando lambdas e high order functions, 
#apresente os 5 maiores valores pares e a soma destes.
#Você deverá aplicar as seguintes funções no exercício:
#map
#filter
#sorted
#sum
#Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
#a lista dos 5 maiores números pares em ordem decrescente;
#a soma destes valores.

def ler_numeros(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return list(map(int, arquivo.readlines()))

is_par = lambda x: x % 2 == 0

numeros = ler_numeros('number.txt')

pares = list(filter(is_par, numeros))

pares_ordenados = sorted(pares, reverse=True)

cinco_maiores = pares_ordenados[:5]

soma_cinco_maiores = sum(cinco_maiores)

print(cinco_maiores)
print(soma_cinco_maiores)