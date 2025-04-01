#6. Escreva um programa que leia um vetor de N números inteiros (N será lido),
#inverta a ordem dos elementos do vetor e exiba o vetor invertido.
#Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
#Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em
#ordem inversa!

N = int(input('Digite o tamanho do Vetor: '))
V = [0] * N

for i in range(N):
    V[i] = int(input(f'Digite o {i + 1} número do vetor: '))

print('Vetor original:', V)

for i in range(N//2):

    V[i], V[(N -1) - i] = V[(N -1) - i], V[i]


print('Vetor invertido:', V)
