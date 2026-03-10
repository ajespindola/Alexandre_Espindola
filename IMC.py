nome = input("Nome: ")
peso = float(input("Peso em Kg: "))
altura = float(input("Altura em metros: ")) 

imc = peso / (altura ** 2)
print(f"{nome}, seu IMC é: {imc:.2f}") 

baixo_peso = imc < 18.5
peso_normal = 18.5 <= imc < 25
sobrepeso = 25 <= imc < 30
obesidade = imc >= 30

if baixo_peso:
  print("Você está abaixo do peso.") 
elif peso_normal:
    print("Você está com o peso normal.") 
elif sobrepeso:
    print("Você está com sobrepeso.") 
else:
    print("Você está com obesidade.") 