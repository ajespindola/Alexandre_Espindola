#Leia o ano de nascimento (int) e imprima a idade estimada. (considere ano atual = 2026).
ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nasc
print(f"Sua idade estimada em {ano_atual} é: {idade} anos.")