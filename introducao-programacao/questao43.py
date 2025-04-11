# Receba uma string do usuário e conte quantas vezes cada caractere aparece nela.
# Armazene o resultado em um dicionário.

palavra = input('Digite uma palavra: ')
palavra = palavra.strip().lower()
dicionario = {}

for letra in palavra:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
    
print(dicionario)