#Utilizando high order functions, implemente o corpo da função conta_vogais. 
#O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
#É obrigatório aplicar as seguintes funções:
#len
#filter
#lambda
#Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

def conta_vogais(texto: str) -> int:
    is_vogal = lambda char: char.lower() in 'aeiou'

    total_vogais = len(list(filter(is_vogal, texto)))

    return total_vogais

texto = "Testando a funcao"
print("Número de vogais:", conta_vogais(texto))