#Escreva um programa que leia um vetor A de N números inteiros (N será lido) e
#um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
#respectivos elementos de a multiplicados por K.
#Ex: A = [1,2,3], K = 5, B = [5,10,15].

N = int(input('Digite o tamanho do vetor: '))
K = int(input('Digite o valor da multiplicação: '))
A = [0] * N
B=[]
for i in range(len(A)):
    A[i] = int(input('Digite os números do vetor A: '))
    B.insert(i, A[i] * K)

print('Primeiro vetor: ', A)
print('Segundo vetor: ', B)