#Escreva um programa que solicite N números inteiros
#e armazene-os em uma lista.
#Utilize estruturas condicionais para criar uma nova
#lista contendo apenas os números positivos.
#Calcule e exiba a média dos números positivos.
#Caso não existam números positivos, exiba uma mensagem apropriada. 

N = int(input('Digite o número de elementos: '))
numeros = []
soma_positivos = 0
qt_positivos = 0

for i in range(N):
    num = int(input(f'Digite o {i + 1} número: '))
    numeros.append(num)
    if num > 0:
        soma_positivos += num
        qt_positivos += 1

media_positivos = soma_positivos / qt_positivos if qt_positivos > 0 else 'Não existem números positivos'
print(media_positivos)
