#Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
min = int(input("Digite a quantidade de minutos: "))
horas = min // 60
resto = min % 60
print(f"{min} minutos equivalem a {horas}h{resto:02d}.")