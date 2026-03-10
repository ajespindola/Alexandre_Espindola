# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= para obter segundos restantes.

seg = int(input("Digite o total de minutos: "))
min = seg
min //= 60
print("Segundos convertidos em minutos: ", min)

segrest = seg
segrest %= 60
print("Segundos restantes: ", segrest)