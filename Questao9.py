opcao = 0

while opcao != 3:
    print("1. Somar dois números")
    print("2. Subtrair dois números")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", num1 + num2)

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", num1 - num2)

    elif opcao == 3:
        print("Programa encerrado")

    else:
        print("Opção inválida")
