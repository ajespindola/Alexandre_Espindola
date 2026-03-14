#Leia o preço de um produto e imprima o preço com 10% de desconto.
preco = float(input("Digite o preço do produto: "))
desc = preco * 0.10
vlr_final = preco - desc
print(f"O preço com 10% de desconto é: R${vlr_final:.2f}.")