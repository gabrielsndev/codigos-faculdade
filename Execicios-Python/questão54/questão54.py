#Faça um programa que receba uma frase do usuário e informe quais letras e quantas vezes cada uma aparece na frase.
from utils import contador

frase = input('Digite uma frase: ')

letras = contador.contador(frase)

for letra, quantidade in letras.items():
        print(f'Letra "{letra}": {quantidade} vezes')
