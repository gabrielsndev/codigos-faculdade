#01) Uma empresa está com uma promoção relâmpago! Para cada R$ 30,00 (trinta reais) em
#compras o cliente receberá 01 (um) cupom. Escreva um programa para ler o valor da
#compra de um cliente e exiba:
#● Quantidade de cupons que ele vai receber;

valor = float(input('Digite o valor da compra: '))

cupom = int(valor // 30)

print(f'Você receberá {cupom} cupons')