#Leia a distância (km) e o tempo (h), calcule a velocidade média.
dist = float(input("Digite a distância em km: "))
tempo = float(input("Digite o tempo em horas: "))
vm = dist / tempo
print(f"A velocidade média é {vm:.2f} km/h.")