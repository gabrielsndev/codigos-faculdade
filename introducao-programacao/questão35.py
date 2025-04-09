#Escreva um programa em python que solicite ao usuário
#N números inteiros e armazene-os em uma lista.
#Utilize estruturas de repetição e condicionais para
#contar a frequência de cada número. Exiba cada número da
#lista e quantas vezes ele aparece.

N = int(input('Digite o número N: '))
numeros = []

for i in range(N):
    num = int(input(f'Digite o {i + 1} número: '))
    numeros.append(num)

for num in numeros:
    qt_vezes = numeros.count(num)
    print(f'O número {num} aparece {qt_vezes} vezes.')