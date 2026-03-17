num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))
num4 = int(input("Digite o quarto número inteiro: "))

numeros = [num1,num2,num3,num4]

print(len(numeros))

alvo = int(input("Digite o número para excluir da lista: "))

if alvo in numeros:
    numeros.remove(alvo)
    print(len(numeros))
else:
    print("Número não consta na lista!")
