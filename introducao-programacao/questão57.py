#Crie um programa que peça 5 números ao usuário, armazene-os em uma tupla e informe qual é o maior e o menor valor digitado

lista = []
for i in range(5):
    lista.append(int(input('Digite um número: ')))
tupla = tuple(lista)

print(tupla)
print(max(tupla), min(tupla))