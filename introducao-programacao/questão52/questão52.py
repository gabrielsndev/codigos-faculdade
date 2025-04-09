# Faça um programa que cadastre mercadorias em uma lista de dicionários.
# Em seguida o usuário poderá listar os produtos cadastrados e também
# dar um aumento percentual em determinado projeto,
# passando seu identificador e o valor percentual.
from utils import cadastro
lista_mercadorias = []

while True:
    mercadoria = input('Mercadoria: ')
    valor = float(input('Valor: '))
    lista_mercadorias = cadastro.cadastrar(mercadoria, valor, lista_mercadorias)
    desejo = input('Digite 1 para parar, 2 para continuar, 3 para listar todos os produtos, 4 aumentar o valor de um produto: ')
    match desejo:
        case '1':
            break
        case '2':
            continue
        case '3':
            for i in lista_mercadorias:
                print(i['nome'])
        case '4':
            nome = input('Digite o valor que deseja aumentar: ')
            percentual = int(input('Digite o valor que deseja aumentar em porcentagem:(Ex: 30) '))
            lista_mercadorias = cadastro.aumentar(lista_mercadorias, nome, percentual)
    