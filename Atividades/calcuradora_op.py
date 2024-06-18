def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == '0':
            break
        elif opcao in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

            if opcao == '1':
                print(f"Resultado: {num1 + num2}")
            elif opcao == '2':
                print(f"Resultado: {num1 - num2}")
            elif opcao == '3':
                print(f"Resultado: {num1 * num2}")
            elif opcao == '4':
                try:
                    print(f"Resultado: {num1 / num2}")
                except ZeroDivisionError:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Essa opção não existe")

calculadora()
