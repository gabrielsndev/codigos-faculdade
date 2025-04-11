#Escreva uma função chamada vertical que receba como parâmetro uma string e
#a exiba na vertical, ou seja, com uma letra em cada linha. Faça também um
#programa para testar a função.

def vertical(str):
    for letra in str:
        print(letra)

string = input('Digite a string: ')

print(vertical(string))
