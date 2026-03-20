agenda = {"Ana":"1111-1111", "Bruno":"2222-2222"}
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")

agenda[nome] = telefone

var = input("Digite o nome do contato a ser alterado: ")
if var in agenda:
    fone = input("Digite o novo telefone: ")
    agenda[var] = fone
else:
    print("Contato não existe na agenda!!!")

remover = input("Digite o nome a ser removido: ")
if remover in agenda:
    agenda.pop(remover)
else:
    print("Contato não existe na agenda!!!")

agenda2 = sorted(agenda.keys())
print(agenda)
print(agenda2)