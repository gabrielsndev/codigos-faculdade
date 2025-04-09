dick = {}

with open('faltas.txt', 'r') as file:
    file = file.read().split('\n')

for linha in file:
    linha = linha.split(';')
    linha = linha[1::]
    for aluno in linha:
        if aluno not in dick:
            dick[aluno] = 1
        else:
            dick[aluno] += 1

print(dick)