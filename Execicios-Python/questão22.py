#Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
#será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
#corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
#o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0
#(zero).
#Ao final, imprima as duas matrizes (no formato de matriz).

import random

N = int(input('Digite a ordem da matriz quadrada: '))
a = []
b = []

for i in range(N):
    a.append([0] * N)
    b.append([0] * N)

for i in range(N):
    for j in range(N):
        a[i][j] = random.randint(0, 20)

for i in range(N):
    for j in range(N):
        if i == j or i + j == N - 1:
            b[i][j] = 0
        else:
            b[i][j] = i + j + a[i][j]

print('Matriz A: ')
for linha in a:
    print(linha)

print('Matriz B: ')
for linha in b:
    print(linha)

