#Considerando que essa empresa realizou 200 (duzentas) vendas em um determinado
# dia. Altere o programa anterior para obter o valor de cada compra e, além das informações
# da questão anterior, também apresentar (ao final):
# ● Total do valor vendido nesse dia;
# ● Quantidade de cupons distribuídos nesse dia;
# ● Maior valor vendido e respectiva quantidade de cupons entregues.

maior = 0 
cupons = 0
total = 0

for i in range(200):
    compra = float(input('Digite o valor da compra: '))
    cupom = int(compra // 30)
    resto = compra % 30 
    prox_cupom = 30 - resto
    total = total + compra

    if maior < compra:
        maior = compra
    else: pass

    if cupom == 0:
        print('Sem cupons!')
    else:
        print(f'Você receberá {cupom} cupons')
        cupons = cupons + cupom
        
maior_cupom = maior // 30

print(f'Este foi o TOTAL vendido: R${total:.2f}')
print(f'Esta foi a quantidade de Cupons distribuidos no dia: {cupons}')
print(f'Este foi o maior valor: R${maior:.2f}')
print(f'E a maior quantidade de cupons distribuidos em uma única compra foi: {int(maior_cupom)}')

