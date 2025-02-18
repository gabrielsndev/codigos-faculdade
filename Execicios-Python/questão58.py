import datetime

#conseguir o ano atual
print(datetime.datetime.now().year)

def cadastrar_motorista():
    nome = input('Nome: ')
    idade = input('Data de nascimento: (**/**/****)')
    idade = idade.split('/')
    try:
        idade[0] = int(idade[0])
        idade[1] = int(idade[1])
        idade[2] = int(idade[2])
    except ValueError:
        return 'Data de nascimento inválida'

    verificar_idade(idade)

def verificar_idade(idade):
    dia = idade[0]
    mes = idade[1]
    ano = idade[2]

    if mes in ['01', '03', '05', '07', '08', '10', '12']:
        if dia <= 31 and mes > 0:
            print('Motorista cadastrado com sucesso!')
        else: print('motorista não cadastrado')

    elif mes == '02':
        if dia <= 28 and mes > 0:
            print('Motorista cadastrado com sucesso!')
        else: print('Motorista não cadastrado')
    
    elif mes in ['04', '06', '09', '11']:
        if dia <= 30 and mes > 0:
            print('Motorista cadastrado com sucesso!')
        else: print('Motorista não cadastrado')

    else: print('A idade informada é inválida')

    datetime.datetime()

#inconcluida







while True:
    print('''
    Escolha uma opção (1 Cadastrar novo motorista, 2 Listar motoristas, 3 sair do programa): ''')

    opcao = input('')

    match opcao:
        case '1':
            print('Opção 1 escolhida')
            cadastrar_motorista()
        case '2':
            print('Opção 2 escolhida')
        case '3':
            print('Opção 3 escolhida')
        case _:
            print('Opção inválida')
            print('Tente novamente.')

