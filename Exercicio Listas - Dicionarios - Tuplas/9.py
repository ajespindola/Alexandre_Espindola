nome = input("Digite o nome: ")
preco = float(input("Informe o preço: "))
qtd = int(input("Digite a quantidade: "))

produto = {"nome":nome, "preco":preco, "qtd":qtd}

aumento = float(input("Digite o percentual de aumento: "))

produto["preco"] += float((produto["preco"] * aumento) / 100)
produto["qtd"] += 2

total = produto["preco"] * produto["qtd"]

print(produto)
print(f"{total:.2f}")