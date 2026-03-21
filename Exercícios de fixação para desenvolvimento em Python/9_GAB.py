# Lê o preço do produto como número decimal
preco = float(input("Digite o preço do produto: "))

# Calcula o valor do desconto
desconto = preco * 10 / 100

# Calcula o novo preço com desconto
preco_final = preco - desconto

# Exibe o preço final
print("Preço com desconto:", preco_final)