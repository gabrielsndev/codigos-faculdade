#Escreva um programa que leia um vetor contendo N elementos inteiros (N será
#lido), calcule e exiba:
#• A quantidade de elementos pares;
#• A quantidade de elementos ímpares;
#• A soma de todos os elementos;
#• A média dos elementos do vetor.

qt_par = 0
N = int(input('Digite o tamanho do vetor: '))
soma = 0
vetor = [0] * N

for i in range(N):
    vetor[i] = int(input(f'Digite um valor para o elemento numero {i + 1} do vetor: '))
    soma += vetor[i]

for i in range(N):
    if ((vetor[i] % 2) == 0):
        qt_par += 1

qt_impar = N - qt_par
media = soma / N

print(f'A quantidade de números pares é: {qt_par}')
print(f'A quantidade de números pares é: {qt_impar}')
print(f'A soma de todos os números é {soma}')
print(f'A média dos elementos do vetor é {media:.2f}')
