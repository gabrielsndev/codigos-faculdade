#5. Escreva um programa que receba um vetor V de N números inteiros (N será lido),
#determine e exiba o maior e o menor elemento deste vetor e seus respectivos
#índices.
#Obs: suponha a inexistência de valores repetidos.
import random
numeros = list(range(1, 20, 2))

random.shuffle(numeros)

maior = menor = numeros[0]
maior_i = menor_i = 0

for i in range(1, len(numeros)):
    if numeros[i] > numeros[maior_i]:
        maior  = numeros[i]
        maior_i = i

    if numeros[i] < numeros[menor_i]:

        menor  = numeros[i]
        menor_i = i

print(numeros)
print(f'O maior valor {maior}, no indice {maior_i}')
print(f'O menor valor {menor}, no indice {menor_i}')
