#Faça um programa em python que solicite números
#ao usuário enquanto ele não digita o valor X, ao digitar o valor X,
#o programa irá calcular a média dos números digitados e imprimir na tela.

n = 0
soma = 0
X = int(input('Digite o valor de X: '))

while True:
    num = int(input('Digite um número: '))

    if num == X:
        break

    soma += num
    n += 1

media = soma / n
print('Média dos números digitados:', media)