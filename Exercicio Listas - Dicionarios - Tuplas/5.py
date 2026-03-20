fila = ["Ana","Bruno"]
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o primeiro nome: ")
fila2 = [nome1,nome2]
fila.extend([nome1])
fila.extend([nome2])
print(fila)

prior = input("Digite o nome prioritário: ")
fila.insert(0, prior)

print(fila)

ultimo = fila.pop(0)
print(fila)
print(f"O último nome da fila era: {ultimo}")