nome = input("Informe o nome: ")
preco = float(input("Digite o preço: "))

produto = {"nome":nome, "preco":preco}
print(produto)
print("desonto" in produto)