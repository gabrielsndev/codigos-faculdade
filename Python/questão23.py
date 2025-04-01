#Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma
#dada matriz.
#Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
#por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].

#Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
#pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
#duas matrizes (no formato de matriz).
import random

a = []
b = []

for i in range(3):
    a.append([0] * 5)

for i in range(5):
    b.append([0] * 3)

for i in range(3):
    for j in range(5):
        a[i][j] = random.randint(0, 10)

for i in range(5):
    for j in range(3):
        b[i][j] = a[j][i]

print('Matriz original: ')
for linha in a:
    print(linha)

print('Matriz transposta: ')
for linha in b:
    print(linha)
    