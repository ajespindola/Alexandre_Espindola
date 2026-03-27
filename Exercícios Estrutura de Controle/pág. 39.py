#Atividade: Sistema de Inventário

inventario = []

while True:
    item = input("Digite o ítem encontrado ou sair: ")
    if item.upper() == "SAIR":
        break
    inventario.append(item)
inventario.sort()
print(inventario)
print(len(inventario))
