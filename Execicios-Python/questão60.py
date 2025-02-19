#Crie uma função que receba dois números e uma operação (soma, subtração, multiplicação ou
#divisão) e retorne o resultado da operação. A função deve suportar operações básicas e tratar
#divisões por zero.


def calcular(num1, num2, operacao):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 'Os valores digitados não são números'

    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Divisão por zero não é permitida'
    else:
        return 'Operação inválida'
    
num1 = input('Digite o primeiro número: ')

num2 = input('Digite o segundo número: ')
operacao = input('Digite o nome da operação (soma, subtração, multiplicação, divisão): ')

print(calcular(num1, num2, operacao))