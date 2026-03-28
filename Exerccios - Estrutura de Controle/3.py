#Solicite ao usuário que informe a sua idade e depois classifique em:
#      a. Menor ou igual a 11 anos = criança.
#      b. Maior do que 11 e menor ou igual a 17 = adolescente.
#      c. Maior do que 17 e menor ou igual a 59 = adulto
#      d. Maior do que 59 = idoso.

idade = int(input("Informe a sua idade: "))
if idade <= 11:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 59:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")    