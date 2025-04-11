#Faça um programa que solicite os dados nome, idade e cpf (utilizando pontuação) de vários
#contato e só permita salvar o usuário em uma lista de dicionários se os dados foram
#preenchidos e se o cpf possuir 11 dígitos excluindo pontos e traços.
#O usuário também poderá listar os usuários cadastrados.
from utils import validacao
lista_usuarios = []

while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    cpf = input('Digite o CPF: ')

    if validacao.valida_cpf(cpf):
        usuario = {'nome': nome, 'idade': idade, 'cpf': cpf}
        lista_usuarios.append(usuario)
        print('Usuário foi cadastrado')
    else:
        print('CPF informado é inválido')
        continue

    desejo = input('Se quiser continuar digite 1, se quiser listar um usuário digite 2, para sair digite 3: ')

    match desejo:
        case '1':
            continue
        case '2':
            for user in lista_usuarios:
                print(user['nome'])
        case '3':
            break
        case _:
            print('Opção inválida')
            print('Por padrão insira um novo usuário: ')
