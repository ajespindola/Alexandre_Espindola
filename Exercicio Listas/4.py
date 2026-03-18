num1 = float(input("Digite o primeiro número inteiro: "))
num2 = float(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite o terceiro número inteiro: "))

lista = [num1,num2,num3]
print(lista)

media = float(sum(lista)/3)
print(media)

if num1 < num2 and num1 < num3:
    menor = float(input(f"A nota {num1} é a menor, digite a nova nota: "))
    lista[0] = menor
elif num2 < num1 and num2 < num3:
    menor = float(input(f"A nota {num2} é a menor, digite a nova nota: "))
    lista[1] = menor
elif num3 < num1 and num3 < num2:
    menor = float(input(f"A nota {num3} é a menor, digite a nova nota: "))
    lista[2] = menor

lista.sort()
media = float(sum(lista)/3)

print(lista)
print(media)