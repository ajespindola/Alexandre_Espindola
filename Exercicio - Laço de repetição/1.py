#Criar um sistema precisa registrar compras realizadas por clientes.

total = 0
quantidade = 0
while True:
    valor = float(input("Digite o valor da compra (ou 0 para encerrar): "))
    
    if valor == 0:
        break
    
    total += valor
    quantidade += 1
if quantidade > 0:
    media = total / quantidade
    print(f"Total das compras: R${total:.2f}")
    print(f"Quantidade de compras realizadas: {quantidade}")
    print(f"Valor médio das compras: R${media:.2f}")
else:
    print("Nenhuma compra foi realizada.")
    