#Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
#Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
#import random 
# amostra aleatoriamente 50 números do intervalo 0...500
#random_list = random.sample(range(500),50)
#Use as variáveis abaixo para representar cada operação matemática:
#mediana
#media
#valor_minimo 
#valor_maximo 
#Importante: Esperamos que você utilize as funções abaixo em seu código:
#random
#max
#min
#sum

import random

random_list = random.sample(range(500), 50)

random_list_ordenada = sorted(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

media = sum(random_list) / len(random_list)

tamanho_lista = len(random_list_ordenada)
if tamanho_lista % 2 == 0:
    mediana = (random_list_ordenada[tamanho_lista // 2 - 1] + random_list_ordenada[tamanho_lista // 2]) / 2
else:
    mediana = random_list_ordenada[tamanho_lista // 2]

print("Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}".format(media, mediana, valor_minimo, valor_maximo))