# Leia um número (int), aplique n %= 2 e imprima.
# 0 = par, 1 = ímpar
num = int(input("Digite o número que para saber se par ou ímpar: "))
num %= 2

print(num)


if num == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")