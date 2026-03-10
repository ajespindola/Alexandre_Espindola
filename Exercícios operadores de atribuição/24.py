# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).
metros = int(input("Digite o total de dias: "))

km = metros
km //= 1000
print("A quantidade Km é: ", km)

mresto = metros
mresto %= 1000
print("O restante em metros é: ", mresto)