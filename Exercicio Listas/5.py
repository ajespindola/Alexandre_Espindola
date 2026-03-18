fila = ["Ana","Bruno"]
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o primeiro nome: ")
fila2 = [nome1,nome2]
fila.extend([nome1])
fila.extend([nome2])
print(fila)
prior = int(input("Digite o prioritário: (1/2/3/4) "))

if prior == 1:
    fila[0] = "Ana"
elif prior == 2:
    fila[0] = "Bruno"
    fila[1] = "Ana"
elif prior == 3:
    fila[0] = nome1
    fila[2] = "Ana"
elif prior == 4:
    fila[0] = nome2
    fila[3] = "Ana"
else:
    print("Número não encontrado!")




print(fila)
