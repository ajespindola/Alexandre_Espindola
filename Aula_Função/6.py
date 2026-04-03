#Crie uma função que receba uma lista de números e retorne a média dos valores.
def calcular_media(lista):
    if not lista:
        return None 
    else:
        return sum(lista) / len(lista)

numeros = []

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    else:
        numeros.append(float(entrada))

media = calcular_media(numeros)

if media is not None:
    print(f"A média dos números é: {media:.2f}")
else:
    print("Nenhum número foi digitado para calcular a média.")