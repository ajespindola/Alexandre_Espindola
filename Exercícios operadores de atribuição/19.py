# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.

estoque = int(input("Digite o total do estoque: "))

estoque -= int(input("Digite o tota de venda: "))
print("Este é o estoque após a venda: ",estoque)

estoque += int(input("Digite o total de reposição: "))
print("Este é o estoque após a reposição: ", estoque)

estoque %= 6
print("Este é o estoque após a reposição dividido por 6: ", estoque)
