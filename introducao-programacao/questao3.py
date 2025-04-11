#A prefeitura de uma cidade fez uma pesquisa com várias pessoas coletando dados sobre a idade e
#o salário de cada uma delas.
#Escreva um programa que leia esses dados acima, calcule e imprima:
#• A média de idade;
#• O menor salário;
#• A quantidade de pessoas com idade de 18 anos e salários até R$ 1.500,00.
#Obs: a leitura da idade 0 (zero) indicará o final dos dados de entrada.

idade =  int(input('Digite sua idade: '))
menor_salario = salario = float(input('Qual seu salário? '))
contador_pessoas = 1
contador_idade = idade
maiores = 0
if idade >= 18 and salario <= 1500.00:
    maiores += 1

while True:
    idade = int(input('Digite sua idade: '))
    if idade == 0:
        break
    salario = float(input('Qual seu salário? '))
    contador_idade += idade
    contador_pessoas += 1

    if menor_salario > salario:
        menor_salario = salario
    
    if idade >= 18 and salario <= 1500.00:
        maiores += 1

media_idade = contador_idade / contador_pessoas

print(f'A média de idades é: {media_idade}')
print(f'O menor salário é: {menor_salario:.2f}')
print(f'A quantidade de pessoas que tem 18 anos e ganham mais de R$ 1500.00 é: {maiores}')