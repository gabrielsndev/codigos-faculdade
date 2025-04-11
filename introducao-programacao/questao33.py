#Escreva um programa em python que leia um número
#inteiro N e gere uma lista com os números de 1 até N.
#Para cada número na lista substitua por "Fizz" se for múltiplo de 3,
#substitua por "Buzz" se for múltiplo de 5, substitua por
#"FizzBuzz" se for múltiplo de 3 e 5 e exiba a lista modificada.


N = int(input('Digite um número inteiro: '))
lista = []

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
       lista.append('FizzBuzz')
    elif i % 3 == 0:
       lista.append('Fizz')
    elif i % 5 == 0:
       lista.append('Buzz')
    else:
       lista.append(i)

print(lista)

