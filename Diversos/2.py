#Enunciado:
#O aluno digita uma nota de 0 a 10. O programa retorna:
#≥ 9 → Excelente
#≥ 7 → Bom
#≥ 5 → Regular
#< 5 → Reprovado

nota = float(input("Digite a nota (0 a 10): "))
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Reprovado")