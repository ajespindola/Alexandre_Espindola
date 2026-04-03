#Crie uma função que receba uma palavra e verifique se ela é um palíndromo
#(lê igual de trás para frente).

def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

var = input("Digite uma palavra: ")

if palindromo(var):
    print(f"'{var}' é um palíndromo.")
else:
    print(f"'{var}' não é um palíndromo.")