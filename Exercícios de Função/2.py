#Crie uma função que receba dois números e retorne a soma deles.
def soma(num1, num2):
    return num1 + num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"A soma de {num1} e {num2} é: {soma(num1, num2)}")