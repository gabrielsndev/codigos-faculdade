#Escreva uma função chamada fatorial que receba como parâmetro um número
#inteiro e retorne seu fatorial. Faça também um programa para testar a função.

def fatorial(num):

    fat = 1
    for i in range(1, num + 1):
        fat = fat * i
    return fat

num = int(input('Digite um número: '))
print(fatorial(num))