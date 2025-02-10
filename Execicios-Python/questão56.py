# Crie uma função que receba uma string e retorne uma lista com todas as palavras em ordem inversa. Exemplo:
# Entrada: "Python é incrível" Saída: ["incrível", "é", "Python"]

def reverter(stringe:str):
    frase = stringe.split()
    frase.reverse()
    return frase

frase = input('Digite uma frase: ')

print(f'A frase invertida é: {reverter(frase)}')
