# Escreva um programa para ler 06(seis)números inteiros
# e imprima:
#   a soma deles
#   quantos deles são maiores que 20
#   a média de números

qt = 0 
soma = 0 

for i in range(6):
    numero = int(input('Número: '))
    soma += numero
    if numero > 20:
        qt += 1

media = soma / (i + 1)
print(f'A soma de todos os números é: {soma}')
print(f'A quantidade de números maiores que 20 é: {qt}')
print(f'A média de todos os número é: {media}')