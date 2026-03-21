# Lê a quantidade de minutos
minutos = int(input("Digite a quantidade de minutos: "))

# Calcula a quantidade de horas inteiras
horas = minutos // 60

# Calcula os minutos que sobraram
minutos_restantes = minutos % 60

# Exibe o resultado no formato pedido
print(horas, "h", minutos_restantes, "min")
