# Escreva uma função chamada calcular_media que recebe uma lista de números como parâmetros e retorna a média dos valores


def calcular_media(*args):
    return sum(*args) // len(*args)

print(calcular_media([10, 9, 8]))