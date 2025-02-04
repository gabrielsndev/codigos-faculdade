#Escreva um programa que imprima a tabuada de um valor lido (de 1 a 10). Por exemplo, se for lido
#o valor 5, a saída deverá seguir o modelo abaixo:
#1 x 5 = 5
#2 x 5 = 10
#3 x 5 = 15
#...
#10 x 5 = 50
#Obs: use a estrutura for.

valor = int(input('Digite um Valor: '))
multiplicador = 1

for i in range(10):
    resultado = valor * multiplicador
    multiplicador += 1
    print(resultado)

