#Classificação de temperatura
'''
1- peça para o usuário digitar a temperatura
2- ler a informação digitada
3- fazer a verificação da temperatura na tabela
4- imprimir a classificação da tabela para o usuário
'''


temp = float(input("Digite a temperatura: "))

if temp < 10:
    print("Muito Frio!!!!")
elif temp < 24:
    print("Agradável =)")
elif temp < 30:
    print("Quente =|")
else:
    print("Muito Quente =(")
