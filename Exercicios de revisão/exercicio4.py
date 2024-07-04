#04) Considerando que essa empresa possui exatamente 1000 (mil) cupons para serem
#distribuídos, altere a questão anterior para distribuir os cupons até que acabe o estoque. Ao
#final, exibir:
#● Quantidade de clientes que receberam todos os cupons da sua compra;
#● Quantidade de cupons não distribuídos, ou seja, sobraram.

qtd_cupons = 1000
clientes_satis = 0
maior = 0 
cupons = 0
total = 0


while qtd_cupons > 0:
    compra = float(input('Digite o valor da compra: '))
    cupom = int(compra // 30)
    qtd_cupons -= cupom

    if qtd_cupons >= cupom:
        clientes_satis = clientes_satis + 1 


print(f'Quantidade de clientes que receberam todos seus cupons: {clientes_satis}')
if qtd_cupons > 0:
    print(f'Quantidade de cupons que sobraram {qtd_cupons}')
else: pass
    








