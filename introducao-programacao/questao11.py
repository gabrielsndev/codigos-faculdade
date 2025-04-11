#Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
#inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.

import random

numeros = [0] * 30
qt = 0

for i in range(len(numeros)):
    numeros[i] = random.randint(0, 10)
    #numeros[i] = int(input('Digite um número: '))

chute = int(input('Chute: '))

for i in range(len(numeros)):
    if chute == numeros[i]:
        qt += 1

print(numeros)
print(qt)

