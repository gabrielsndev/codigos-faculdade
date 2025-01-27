# Faça um programa que receba o nome completo
# e retorne o primeiro e o último nome, depois imprima o nome
# com as vogais substituidas por *.

nome = input('Digite seu nome completo: ')
nome_split = nome.split()
primeiro_nome = nome_split[0]
ultimo_nome = nome_split[-1]

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for letra in nome:
    if letra in vogais:
        nome = nome.replace(letra, '*')

print(f'Nome formatado: {primeiro_nome} {ultimo_nome}')
print(nome)