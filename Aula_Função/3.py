#Crie uma função que receba um número e informe se ele é PAR ou ÍMPAR. 

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"

num = int(input("Digite um número: "))
resultado = par_ou_impar(num)

print(f"O número {num} é {resultado}.")