#Leia o raio de um círculo (float) e calcule a área, utilize π = 3.14.
r = float(input("Digite o raio do círculo: "))
pi = 3.14
area = pi * (r ** 2)
print(f"A área do círculo com raio {r} é {area:.2f}.")