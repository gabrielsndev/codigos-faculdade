#Receba uma lista de tuplas contendo o nome do aluno e suas notas em três provas.
#Crie um dicionário onde a chave seja o nome do aluno e o valor seja "Aprovado" se sua média for maior ou igual a
#7, ou "Reprovado" caso contrário.

lista = [(input('Nome do aluno: '), (int(input('nota 1: ')),int(input('nota 2: ')), int(input('nota 3: '))))]
dic = {}

while True:
    opcao = input('Vai inserir outro aluno? (S/N): ')
    if opcao.upper() == 'N':
        break
    else:
        lista.append((input('Nome do aluno: '), (int(input('nota 1: ')), int(input('nota 2: ')), int(input('nota 3: ')))))

for aluno in lista:
    nome = aluno[0]
    notas = aluno[1]
    media = sum(notas) // 3
    if media >= 70:
        status = 'Aprovado'
    else:
        status = 'Reprovado'
    dic[nome] = status

print(dic)
