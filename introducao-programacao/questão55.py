#Escreva um programa que peça ao usuário para digitar uma frase e conte quantas palavras possuem mais de 5 caracteres.
maiores = []
menores = []
frase = input('Digite uma frase:')
frase = frase.split(' ')
for palavra in frase:
    if len(palavra) > 5:
        maiores.append(palavra)
    else:
        menores.append(palavra)

print(f'Palavas com mais de 5 letras: {maiores}')
print(f'Palavrsa com menos de ou com 5 letras: {menores}')
