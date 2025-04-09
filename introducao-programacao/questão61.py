#Crie um programa em que seja possível cadastrar contas de banco como dicionários contem número,
#nome do titular e o valor. Faça com que seja possível transferir um valor de uma para outra e caso a conta de origem não tenha saldo
#uma exceção deve ser lançada e a mensagem de erro deve ser retornada. Também será possível depositar valores nas contas informando o número.

contas = {}

def cadastrar_conta(numero, titular, saldo):
    if numero in contas:
        return Exception('Já existe uma conta com esse número.')
    contas[numero] = {'titular': titular,'saldo': saldo}
    return 'Conta cadastrada com sucesso.'

def transferir(numero_origem, numero_destino, valor):
    if numero_origem not in contas or numero_destino not in contas:
        return Exception('Número de conta inválido.')
    if contas[numero_origem]['saldo'] < valor:
        return Exception('Saldo insuficiente.')
    contas[numero_origem]['saldo'] -= valor
    contas[numero_destino]['saldo'] += valor
    return 'Transferencia efetuada com sucesso!'

def depositar(numero, valor):
    if numero not in contas:
        return Exception('Número de conta inválido.')
    contas[numero]['saldo'] += valor
    return 'Depósito efetuado com sucesso!'


while True:
    print('Menu: ')
    print('1 - Cadastrar Conta')
    print('2 - Transferir')
    print('3 - Depositar')
    print('4 - Sair')
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            numero = int(input('Número da conta: '))
            titular = input('Nome do titular: ')
            saldo = float(input('Saldo inicial: '))
            print(cadastrar_conta(numero, titular, saldo))
        case 2:
            numero_origem = int(input('Número da conta de origem: '))
            numero_destino = int(input('Número da conta de destino: '))
            valor = float(input('Valor a transferir: '))
            print(transferir(numero_origem, numero_destino, valor))
        case 3:
            numero = int(input('Número da conta: '))
            valor = float(input('Valor a depositar: '))
            print(depositar(numero, valor))
        case 4:
            break
        case _:
            print('Opção inválida.')



