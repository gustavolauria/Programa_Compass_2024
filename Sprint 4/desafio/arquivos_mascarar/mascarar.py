import hashlib

def calcular_hash(string):
    hash_obj = hashlib.sha1()
    hash_obj.update(string.encode('utf-8'))
    return hash_obj.hexdigest()

if __name__ == "__main__":
    while True:
        string = input("Digite uma string (ou 'exit' para sair): ")
        if string.lower() == 'exit':
            break

        hash_str = calcular_hash(string)
        print("O hash SHA-1 da string é:", hash_str)