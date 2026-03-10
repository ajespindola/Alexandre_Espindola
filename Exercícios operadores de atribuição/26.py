# Leia dois inteiros a e b. Em a: a += b, a *= 2, a %= 7.
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

a += b
print("Valor de a += b : ", a)

a *= 2
print("Valor a *= 2 é: ", a)

a %= 7
print("Valor a %= 7 é: ", a)