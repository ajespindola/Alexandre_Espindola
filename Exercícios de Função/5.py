#Crie uma função que receba uma string e retorne a quantidade de caracteres que ela possui.
def contar_caracteres(qualquer):
    return len(qualquer)

entrada = input("Digite uma string: ")
quantidade = contar_caracteres(entrada)

print(f"A string '{entrada}' possui {quantidade} caracteres.")
