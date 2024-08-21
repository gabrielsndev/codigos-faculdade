#Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
#• Os números que estão nos índices pares;
#• Os números que estão nos índices ímpares.

numeros = [0] * 10

for i in range(10):
    numeros[i] =  int(input('Digite um número: '))

for i in range(10):
    if i % 2 == 0:
        print(f'Número na posição par {i} é: {numeros[i]}')
    else:
        print(f'Número na posição impar {i} é: {numeros[i]}')

print(numeros)
