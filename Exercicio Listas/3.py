num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

lista = [num1,num2,num3]
soma = int(sum(lista[:2]))
lista[2] = soma
print(lista)