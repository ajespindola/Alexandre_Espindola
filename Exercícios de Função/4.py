#Crie uma função que receba uma lista de números e retorne o maior número da lista.
lista = []

def maior_numero(lista):
    return max(lista)

n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))
n3 = int(input("Digite o número: "))
lista = [n1, n2, n3]

maior = maior_numero(lista)
print("O maior número da lista é:", maior)