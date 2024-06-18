def calcular_idade(nasc):
    return 2022 - nasc

def ano_valido():
    while True:
        try:
            ano = int(input("Digite o seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano inválido. Por favor, tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    nome_completo = input("Digite o seu nome completo: ")
    nasc = ano_valido()
    idade = calcular_idade(nasc)
    print(f"{nome_completo}, você completou ou completará {idade} anos em 2022.")

if __name__ == "__main__":
    main()
