f1 = int(input("Digite o primeiro número: "))
f2 = int(input("Digite o segundo número: "))
f3 = int(input("Digite o terceiro número: "))
f4 = int(input("Digite o quarto número: "))

num = (f1, f2, f3, f4)

print(f"A Tupla original é: {num}")
num2 = sorted(num)
print(f"Tipo da variável ordenada é: {type(num2)}")