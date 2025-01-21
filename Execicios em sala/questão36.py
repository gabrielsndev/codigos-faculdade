# crie um programa que receba uma tupla de números inteiros fornecida pelo usuário e determine:
# quantas vezes o número 5 aparece na tupla, 
# a posição do número 3 (se existir), 
# todos os números maiores que 10

utils = []

while True:
    teste = input(" Digite um elemento para tupla: (para parar digite '.') ")
    if teste == '.':
        break
    utils.append(int(teste))

tupla = tuple(utils)

print(f'número de vezes que o 5 aparece: {tupla.count(5)}')
if 3 in tupla:
    print(f'índice do primeiro número 3: {tupla.index(3)}')
soma = 0
for i in tupla:
    if i > 10 :
        soma += 1
print(f'somados números maior que 10: {soma}')