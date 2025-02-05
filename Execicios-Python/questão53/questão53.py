# Faça um programa que receba o peso e a altura de um indivíduo e calcule seu imc através de uma função. 
# imc = Peso dividido pela altura ao quadrado.
from utils import imc

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

print(f'seu imc é {imc.imc(peso, altura)}')