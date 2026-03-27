#Classificação de notas

'''
1- peça para o usuário digitar a nota
2- ler a informação digitada
3- fazer a verificação da nota na tabela
4- imprimir a classificação da tabela para o usuário
'''


nota = float(input("Digite a nota: "))

if nota < 5:
    print("Reprovado")
elif nota < 7:
    print("Recuperação")
elif nota < 9:
    print("Aprovado")
else:
    print("Aprovado com excelência")
