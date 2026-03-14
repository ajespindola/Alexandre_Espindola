#Leia um número como string e imprima o seu tipo antes e depois de converter para int.
num1 = input("Digite um número: ")
print(f"O tipo antes da conversão é {type(num1)}.")
num2 = int(num1)
print(f"O tipo depois da conversão é {type(num2)}.")