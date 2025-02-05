# Faça um programa que receba do usuário a quantidade de caracteres e gere uma senha segura para o mesmo.
# O usuário também terá a opção de informar se quer a senha só com números, com números e letras ou números, letras e caracteres especiais.
# Para isso deve ser criada uma função chamada gerar_senha que se encontra em um módulos chamado utils/password.
from utils import password



qtd_caract = int(input('Digite a quantidade de caracteres: '))

modo = input('1: Letras e caracteres especiais, 2: Apenas números, 3: Números e letras: ')

match modo:
    case '1':
        senha = password.gerar_senha(modo, qtd_caract)
        print(senha)

    case '2':
        senha = password.gerar_senha(modo, qtd_caract)
        print(senha)

    case '3':
        senha = password.gerar_senha(modo, qtd_caract)
        print(senha)