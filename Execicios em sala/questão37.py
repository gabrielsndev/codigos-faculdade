#Dado um extrato que veio do banco, crie um programa que leia os dados e calcule o saldo do indíviduo:

saldo = 0
data = '''01/01/2025 Pix para Joãozinho -50,00
02/01/2025 Pix para Mariazinha -30,00
03/01/2025 Recebimento do salário 1000,00
03/01/2025 Gasolina -200,00
04/01/2025 Hambúrguer sebosão -40,00'''
data = data.split('\n')


for i in data:
    utils = i.split(' ')[-1]
    utils = utils.replace(',', '.')
    utils = float(utils)
    if utils > 0:
        saldo += utils
    else:
       saldo += utils


print(saldo)