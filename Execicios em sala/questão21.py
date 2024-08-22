#Escreva um programa que:
#• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
#inteiros (N será lido);
#• Exiba a matriz lida (no formato de matriz);
#• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.

import random

matriz = []

N = int(input('Digite a ordem da matriz quadrada: '))

for i in range(N):
    matriz.append([0] * N)
    for j in range(N):
        matriz[i][j] = random.randint(1, 10)

print('Matriz:')
for linha in matriz:
    print(linha)

for i in range(N):
    print(matriz[i][i])

