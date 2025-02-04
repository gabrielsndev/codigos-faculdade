# Crie uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade. Depois
# percorra a lista e utilize uma estrutura condicional para criar um dicionário que classifique
# as pessoas em maiores e menores de idade.

pessoas = []

while True:
    nome = input('Digite o nome da pessoa (para parar digite "fim"): ')
    if nome == 'fim':
        break
    idade = int(input('Digite a idade da pessoa: '))
    pessoas.append((nome, idade))

dicionario = {}

for nome, idade in pessoas:
    if idade >= 18:
        dicionario['maiores'] = dicionario.get('maiores', []) + [nome]
    else:
        dicionario['menores'] = dicionario.get('menores', []) + [nome]

print('Pessoas maiores de idade:', dicionario.get('maiores', []))

print('Pessoas menores de idade:', dicionario.get('menores', []))
