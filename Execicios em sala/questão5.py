#Altere o programa da questão 4 para utilizar Vetores(Listas)
#e descobrir quantos números são maiores que a média de todos

qt = 0 
qt_media = 0
soma = 0 
numeros=[0, 0, 0, 0, 0, 0]

for i in range(6):
    numeros[i] = int(input('Número: '))
    soma += numeros[i]
    if numeros[i] > 20:
        qt += 1

media = soma / (i + 1)

for i in range(6):
    if numeros[i] > media:
        qt_media += 1

print(f'A soma de todos os números é: {soma}')
print(f'A quantidade de números maiores que 20 é: {qt}')
print(f'A média de todos os número é: {media:.2f}')
print(f'A quantidade de valores que são acima da média é: {qt_media}')