#Crie uma função que receba uma lista de números e retorne o maior número da lista.
lista = []

def maior_numero(lista_func):
    if not lista_func:
        return None 
    else:
        lista_func.sort(reverse=True)
        return lista_func[0]
    
while True:
    num = input("Digite um número (ou 'sair' para encerrar): ")
    if num == 'sair':
        break
    else:
        lista.append(float(num))
        
print(f"O maior número da lista é: {maior_numero(lista)}")
        