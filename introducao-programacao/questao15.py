#Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão
#lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a
#intercalação dos elementos de A e B.
#Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]
N = int(input('Digite o tamanho dos vetores: '))
A = [0] * N
B = [0] * N
C = []

for i in range(N):
    A[i] = int(input(f'Digite um valor para o elemento numero {i + 1} do vetor A: '))
    B[i] = int(input(f'Digite um valor para o elemento numero {i + 1} do vetor B: '))
    C.append(A[i])
    C.append(B[i])

print(f'Vetor A é: {A}')
print(f'Vetor B é: {B}')
print(f'Vetor C é: {C}')

