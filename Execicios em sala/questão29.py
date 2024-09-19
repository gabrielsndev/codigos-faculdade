#a data no formato “aaaammdd” seguido do
#símbolo “_” e da primeira parte e da última parte do nome do cliente (ambas com a inicial em
#maiúsculo e o restante em minúsculo).
#Exemplo:
#• Data atual: 05/12/2023
#• Cliente: ANTONIO CARLOS PEREIRA SILVA
#• Identificador Gerado: 20231205_AntonioSilva
#Escreva um programa que leia a data atual (no formato “dd/mm/aaaa”) e o nome completo do
#cliente, gere e imprima o respectivo identificador.

nome = input("Digite o seu nome: ").title()
data = input("Digite a data da entrega: ")
dataS = data.split("/")
nomeS = nome.split(" ")
iden = f'{dataS[2] + dataS[1] +dataS[0]}_{nomeS[0] + nomeS[-1]}'


print(f'Data Atual: {data}')

print(f'Cliente: {nome.upper()}')
print(f"Identicador: {iden}")