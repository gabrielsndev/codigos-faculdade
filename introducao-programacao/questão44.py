# Crie um dicionário que representa o estoque de produtos de uma loja (chave: nome do produto, valor: quantidade).
# Permita que o usuário adicione novos produtos,
# atualize quantidades e remova produtos usando um menu interativo (com laços de repetição e estruturas condicionais).

dicionario = {}

dicionario[input('Nome do produto: ')] = float(input('Valor do produto: '))

while True:
    print('Para adicionar um produto digite o número 1 ---')
    print('Para atualizar a quantidade de um produto digite o número 2 ---')
    print('Para remover um produto digite o número 3 ---')
    print('Para sair digite o número 4 ---')
    opcao = int(input('Opção: '))
    
    if opcao == 1:
        nome_do_produto = input('Nome do produto: ')
        valor_do_produto = float(input('Valor do produto: '))
        dicionario[nome_do_produto] = valor_do_produto
    
    elif opcao == 2:
        nome_do_produto = input('Nome do produto: ')
        if nome_do_produto in dicionario:
            quantidade_do_produto = float(input('Nova quantidade do produto: '))
            dicionario[nome_do_produto] = quantidade_do_produto
        else:
            print('Produto não encontrado.')
    
    elif opcao == 3:
        nome_do_produto = input('Nome do produto: ')
        if nome_do_produto in dicionario:
            del dicionario[nome_do_produto]
        else:
            print('Produto não encontrado.')

    elif opcao == 4:
        break

print(dicionario)

