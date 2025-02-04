# Dado um número informado pelo usuário sapara em duas listas os números menores
# ou iguais a ele que são primos e os múmeros menores ou iguais a ele que não são
# primos. Utilize uma função que verifica se o número é primo

numero = int(input('Digite um número: '))
lista_primos = []
lista_tios = []

def eh_primo(numero):
    if numero < 2: return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    
for  i in range(2, numero):
    if eh_primo(i):
        lista_primos.append(i)
    else: lista_tios.append(i)

print(lista_primos)
print(lista_tios)