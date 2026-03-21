# Lê o salário atual
salario = float(input("Digite o salário: "))

# Lê o percentual de aumento
percentual = float(input("Digite o percentual de aumento: "))

# Calcula o valor do aumento
aumento = salario * percentual / 100

# Calcula o novo salário
novo_salario = salario + aumento

# Exibe o novo salário
print("Novo salário:", novo_salario)
