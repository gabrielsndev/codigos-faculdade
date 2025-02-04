#Escreva um programa para declarar uma matriz com tamanho 3x4 e armazene valores aleatórios nessa matriz
import random
matriz = []
for i in range(3):
    matriz.append([0] * 4)

for i in range(3):
    for j in range(4):
        matriz[i][j] = random.randint(0, 20)

for i in range(3):
    print(i, matriz[i])