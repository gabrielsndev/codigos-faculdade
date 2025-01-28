# Escreva um programa que receba uma lista de palavras do usuário e crie um dicionário onde a chave
# seja a palavra e o valor seja um booleano indicando
# se a palavra é um palíndromo (ou seja, se lê o mesmo de trás para frente).

palavras = input('Digite as palavras (separe-as com espaço): ').split()
dicionario = {}

for palavra in palavras:
    if palavra == palavra[::-1]:
        dicionario[palavra] = True
    else:
        dicionario[palavra] = False

print(dicionario)


