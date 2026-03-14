#Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("Digite o salário atual: "))
perc = float(input("Digite o percentual de aumento: "))
aumento = salario * (perc / 100)
novosal = salario + aumento
print(f"O novo salário após um aumento de {perc}% é: R${novosal:.2f}.")