nome = "Juca da Silva"
idade = 40
endereco = "Rua das penas-10"
dtnascimento = "23/05/1985"

print(f'nome: {nome}, idade: {idade}, endereço: {endereco}, Data Nascimento: {dtnascimento}')

print(type(nome))
print(type(idade))
print(type(endereco))
print(type(dtnascimento))

listadecompras = ["arroz", "macarrão", "carne"]
print(f'lista de compras: {listadecompras}')
print(type(listadecompras))

aluno = {
    "nome": "Juca da Silva",
    "idade": 40,
    "endereco": "Rua das penas-10",
    "dtnascimento": "23/05/1985"
}
print(aluno)

nome = input("Digite o nome: ")
idade = input("Digite a idade:")
endereco = input("Digite o endereço:")
dtnascimento = input("Digite a data de nascimento (dd/mm/aaaa)")
print("Olá, ",nome)
print("Sua idade é: ",idade)
print("Seu endereço é: ",endereco)
print("Sua Data de Nascimento é: ",dtnascimento)
confirma = input("você confirma a informação? (S/N):")