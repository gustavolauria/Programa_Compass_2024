import csv

list = ["cachorro", "gato", "elefante", "leao", "tigre", "girafa",
         "zebra", "hipopotamo", "macaco", "panda", "rato",
           "passaro", "cobra", "jacare", "peixe", "tartaruga", "coruja", "gaviao", "puma", "urso"]

list.sort()
[print(animal) for animal in list]

nome_arquivo = "list_animais.csv"

with open(nome_arquivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    for animal in list:
        writer.writerow([animal])

print("Concluido")