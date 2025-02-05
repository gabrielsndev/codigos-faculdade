from matematica import div, multi, soma, sub

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
operacao = input('Qual a operação? (+, -, /, *)')

match operacao:
    case '+':
        print(soma.soma(num1, num2))
    case '-':
        print(sub.sub(num1, num2))
    case '*':
        print(multi.multi(num1, num2))
    case '/':
        print(div.div(num1, num2))
