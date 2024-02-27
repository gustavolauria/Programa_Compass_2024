#Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
#Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
#Importante: Aplique a função range().

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num)