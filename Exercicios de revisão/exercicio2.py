
#02) Altere o programa anterior para verificar se ao calcular a quantidade de cupons ficou
#algum saldo remanescente. Caso tenha ficado, calcular e exibir:
#● Saldo que ele possui para completar mais 1 cupom;
#● Valor que ele deve acrescentar (gastar) para ganhar mais 1 cupom.

valor = float(input('Digite o valor da compra: '))

cupom = int(valor // 30)
resto = valor % 30 
prox_cupom = 30 - resto

print(f'Você receberá {cupom} cupons')
print(f'R$ {resto} de saldo')
print(f'R$ {prox_cupom:.2f} para novo cupom')
