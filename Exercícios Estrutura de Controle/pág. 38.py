#Atividade prática: Sistema de Médias

notas = []

while True:
    contador = int(1)
    num = float(input("Digite a nota: "))
    
    if num < 0:
        print("Você digitou um número inválido e saiu do sistema.")
        break              
    
    notas.insert(contador,num)
    contador += 1
    
    sair = input("Deseja sair S/N: ")
    if sair.upper() == "S":
        print("As notas são: ", notas)
        media = float(sum(notas)) / len(notas)
        print(f"A média das notas é: {media:.2f}")
        if media >= 7:
            print("Situação: APROVADO")
        else:
            print("Situação: RECUPERAÇÃO")
        break