#Escreva um programa que receba uma lista de números do usuário e implemente uma função soma_lista(numeros)
#que recebe essa lista de strings contendo números e retorna a soma dos números convertidos para inteiros.
#Se algum elemento não puder ser convertido, ignore-o e continue a soma.

def soma_lista(numeros):
    soma = 0
    for numero in numeros:
        try:
            soma += int(numero)
        except ValueError:
            pass
    return soma            

numeros = input('Digite uma lista de numeros separados por (" "): ').split(' ')

print(soma_lista(numeros))  