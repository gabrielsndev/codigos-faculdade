
# Receba uma lista de frases e uma palavra do usuário.
# Use um laço de repetição para verificar em quais frases a palavra aparece e armazene as frases em uma nova lista.

frases = input('Digite frases separadas por ",":').split(',')

palavra = input('Digite a palavra: ')

frases_palavra = []
for frase in frases:
    if palavra in frase:
        frases_palavra.append(frase)

print(f'Frases com a palavra: {frases_palavra}')