f1 = input("Digite a primeira fruta: ")
f2 = input("Digite a segunda fruta: ")
f3 = input("Digite a terceira fruta: ")

frutas = (f1, f2, f3)

var = input("Digite o nome da fruta a ser pesquisada: ")

if var in frutas:
    print("Fruta está na tupla!!!")
else:
    print("Fruta não está na tupla!!!")