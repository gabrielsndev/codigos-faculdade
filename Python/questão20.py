#Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
#valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
#deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
#Ao final, exiba as 3 matrizes (no formato de matriz).

import random
#Declarei duas listas vazias
matriza = [] 
matrizb = [] 
matrizc = [] 


#for i in range(Números de Linhas da Matriz)
for i in range(2):
    #matriz.append([0] * 3) ADICIONANDO NA LISTA UMA OUTRA LISTA COM VALOR 0 isso 3 vezes (NÚMERO DE COLUNAS)

    matriza.append([0] * 3)
    matrizb.append([0] * 3)
    matrizc.append([0] * 3)

for i in range(2):
    for j in range(3):
        matriza[i][j] = random.randint(1, 10)
        matrizb[i][j] = random.randint(1, 10)

for i in range(2):
    for j in range(3):
        matrizc[i][j] = matriza[i][j] + matrizb[i][j]


print('Matriz A')
for linha in matriza:
    print(linha)

print('Matriz B')
for linha in matrizb:
    print(linha)

print('Matriz C')
for linha in matrizc:
    print(linha)

