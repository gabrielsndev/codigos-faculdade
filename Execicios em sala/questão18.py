#Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
#lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
#informe em que posição (índice).
#Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
#aparece.
import random

N = int(input('Digite o tamanho do valor: '))

V = [0] * N

for i in range(N):
    #V[i] = int(input(f'Digite o {i+1}º valor: '))
    V[i] = random.randint(1, 10)

K = int(input('Digite um número de 0 a 10 que você ache que esteja no Vetor: '))


for i in range(N):
    if V[i] == K:
        print(f'O número {K} está dentro do vetor! Na posição {i}')


print(V)