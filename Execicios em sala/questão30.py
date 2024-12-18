#Faça um programa que receba primeiramente a quantidade de idades que serão fornecidas.
#Em seguida, receba a quantidade de idades informada e imprima quantos são menores de idade (idade < 18),
#quantos são adultos (idade entre 18 e 60) e quantos são idosos (idade >= 60).

quantidade_idades = int(input('Digite a quantidade de idades: '))
menores = 0
adultos = 0
idosos = 0

for i in range(quantidade_idades):
    idade = int(input(f'Digite a idade do {i+1}º individuo: '))

    if idade < 18:
        menores += 1
    elif idade >= 18 and idade <= 60:
        adultos += 1
    else:
        idosos += 1

print(f'Menores de idade: {menores}')
print(f'Adultos: {adultos}')
print(f'Idosos: {idosos}')