#Escreva um programa que:
#• Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma
#turma e a média de cada um deles.
#o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
#o As médias serão calculadas e armazenadas na 4a coluna da matriz.
#• Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
#• Calcule e imprima a média geral da turma.
#• Calcule e imprima o número de alunos com média superior à média geral da turma.

import random

matriz = []
qt = 0

for i in range(20):
    matriz.append([0] * 4)

for i in range(20):
    for j in range(3):
        #matriz[i][j] = int(input('Digite a nota do aluno'))
        matriz[i][j] = random.randint(0,10)

for i in range(20):
    for j in range(4):
        qt += matriz[i][j]
    
    media = qt // 3
    matriz[i][3] = media
    qt = 0


for i in range(20):
    for j in range(1):
        qt += matriz[i][3]

media_geral = qt // 20
media = 0
qt = 0
for i in range(20):
    for j in range(1):
        if matriz[i][3] > media_geral:
            qt += 1

print('NOTAS E MÉDIAS: ')

for linha in matriz:
    print(linha)

print(f'Média geral da turma: {media_geral}')
print(f'Quantidade de alunos com nota superior a média geral: {qt}')

