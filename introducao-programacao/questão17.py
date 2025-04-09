#Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão
#lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a
#intercalação dos elementos de A e B.

numeros = int(input('Digite o tamanho dos vetores: '))

A = [0] * numeros
B = [0] * numeros

C = [0] * (numeros * 2)

for i in range(numeros):
    A[i] = int(input(f'Digite {i+1} valor de A: '))
    B[i] = int(input(f'Digite {i+1} valor de B: '))

for i in range(numeros):
    C[i * 2] = A[i]
    C[i * 2 + 1] = B[i]

print('Vetor C:', C)