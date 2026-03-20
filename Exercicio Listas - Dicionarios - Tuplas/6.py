nome = input("Digite o nome do Aluno: ")
idade = input("Digite a idade: ")
sexo = input("Masculino ou Feminino M/F: ")
endereco = input("Digite o endereço: ")

aluno = {"nome":nome,"idade":idade,"Sexo":sexo,"Endereço":endereco}

print(f" {aluno}, {type(aluno)}")