# Leia dias (int). Mantenha apenas os dias restantes após converter para semanas (7 dias) usando %=.
dias = int(input("Digite o total de dias: "))
dias %= 7

print("Os total de dias restantes são: ", dias)