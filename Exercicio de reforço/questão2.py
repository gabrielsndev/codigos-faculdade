#Escreva um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#• "Telefonou para a vítima?"
#• "Esteve no local do crime?"
#• "Mora perto da vítima?"
#• "Devia para a vítima?"
#• "Já trabalhou com a vítima?"
#Todas as respostas devem ser apenas "S" (para "Sim") ou "N" (para "Não").
#O programa deve, no final, imprimir uma classificação sobre a participação da pessoa no crime. Se
#a pessoa responder "S" a 2 perguntas ela deve ser classificada como "Suspeita", entre 3 e 4 como
#"Cúmplice" e 5 como "Assassino". Caso contrário, ela será classificada como "Inocente".

perg1 = input('Telefonou para a vítima? (Responda com S para sim e N para não)')
perg2 = input('Esteve no local do crime (Responda com S para sim e N para não)')
perg3 = input('Mora perto da vítima? (Responda com S para sim e N para não)')
perg4 = input('Devia para a vítima? (Responda com S para sim e N para não)')
perg5 = input('Já trabalhou com a vítima? (Responda com S para sim e N para não)')

perg1 = perg1.upper()
perg2 = perg2.upper()
perg3 = perg3.upper()
perg4 = perg4.upper()
perg5 = perg5.upper()

resultado = 0

if perg1 == 'S':
    resultado += 1

if perg2 == 'S':
    resultado += 1

if perg3 == 'S':
    resultado += 1

if perg4 == 'S':
    resultado += 1

if perg5 == 'S':
    resultado += 1

if resultado == 5:
    print('Assasino')
    
elif resultado == 3 or 4:
    print('Cúmplice')

elif resultado == 2:
    print('Suspeito')

elif resultado == 0 or 1:
    print('Inocente')
