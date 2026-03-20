f1 = float(input("Digite a primeira nota: "))
f2 = float(input("Digite a segunda nota: "))
f3 = float(input("Digite a terceira nota: "))

notas = (f1, f2, f3)

print(notas)

media = sum(notas) / len(notas)
print(f"A média é: {media:.2f}")