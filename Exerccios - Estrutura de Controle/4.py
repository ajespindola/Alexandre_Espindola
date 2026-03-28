#Solicite ao usuário que informe um número e depois exiba se é par ou ímpar.

numero = int(input("Informe um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")