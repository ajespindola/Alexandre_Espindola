#Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação.
# Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.

while True:
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
    operacao = input("Informe a operação que deseja realizar (+, -, /, *): ")

    if operacao == "+":
        resultado = numero1 + numero2
        print(f"O resultado da soma é: {resultado}")
    elif operacao == "-":
        resultado = numero1 - numero2
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == "*":
        resultado = numero1 * numero2
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Por favor, informe uma operação válida (+, -, /, *).")

    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        break