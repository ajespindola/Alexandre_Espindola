# Leia base (float). Aplique *= 1.05 (aumento 5%), depois -= 2 (taxa), depois /= 2.
base = float(input("Digite a base: "))

base *= 1.05
print("Base aplicada 5%: ", base)

base -= 2
print("Base menos a taxa: ", base)

base /= 2
print("Base dividida por 2: ", base)