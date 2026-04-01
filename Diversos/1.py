#Instruções
#Enunciado:
#Peça para o aluno digitar a idade de uma pessoa e o programa deve classificar:
#0–12 → Criança
#13–17 → Adolescente
#18–59 → Adulto
#60+ → Idoso

idade = int(input("Digite a idade da pessoa: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")

