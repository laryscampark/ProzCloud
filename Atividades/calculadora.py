def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else 'Erro: Divisão por zero'
    else:
        return 0

# Exemplo de uso:
resultado = calculadora(25, 8, 1) # Soma
print(resultado) # Saída: 33
