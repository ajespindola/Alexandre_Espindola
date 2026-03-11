#Código para executar o cálculo do IMC e dar o resultado na tela

nome = input("Digite o nome: ")
peso = float(input("Informe o peso em Kg: "))
altura = float(input("Informe a altura em metros (ex 1.75): ")) 

imc = peso / (altura ** 2)
print(f"{nome} , O seu IMC é: {imc:.2f}") 

baixo_peso = imc < 18.5
peso_normal = 18.5 <= imc < 25
sobrepeso = 25 <= imc < 30
obesidade = imc >= 30

i = input("Você tem certeza em ver o resultado? (S/N): ").upper()
#print(i)
if i == "S":
    if baixo_peso:           
        print("Você está abaixo do peso.") 
    elif peso_normal:
        print("Você está com o peso normal.") 
    elif sobrepeso:
        print("Você está com sobrepeso.") 
    else:
        print("Você está com obesidade.")
else:
    print("Você fez uma boa escolha!!! =D")