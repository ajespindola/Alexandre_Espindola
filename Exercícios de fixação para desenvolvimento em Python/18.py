#Leia um nome e uma nota (float), com uma casa decimal, e imprima:
#Aluno <nome> ficou com nota <nota>
nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))
print(f"Aluno {nome} ficou com nota {nota:.1f}.")