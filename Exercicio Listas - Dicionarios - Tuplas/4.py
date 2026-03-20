num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))

lista = [num1, num2, num3]
print(f"Números iniciais: {lista}")

media = sum(lista) / len(lista) # Usa o tamanho da lista para ter flexibilidade
print(f"Média inicial: {media:.2f}")

# Menor número no menor indice
menor_valor = min(lista)
indice_menor = lista.index(menor_valor)

# Novo valor para o menor número
nova_nota = float(input(f"O número {menor_valor} é o menor. Digite um novo valor para ele: "))

# substituir o menor valor pelo novo valor
lista[indice_menor] = nova_nota

lista.sort() # ordena a lista em ordem crescente
media_atualizada = sum(lista) / len(lista)

print(f"Números atualizados e ordenados: {lista}")
print(f"Nova média: {media_atualizada:.2f}")