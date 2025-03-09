# Faça um sistema de controle de estoque. O sistema deve apresentar o seguinte menu:

# 1. Incluir produto (O sistema deve gerar um identificador pra ele, e devem ser registrados o nome, a quantidade e o valor de compra, o sistema deve calcular também o preço de venda, sendo 10% a mais que o valor da compra).
# 2. Listrar produtos no estoque (O sistema deve listar todos os produtos cadastrados).
# 3. Buscar produto por nome (O sistema deve ser capaz de recuperar um produto no estoque pelo seu nome ou parte do nome).
# 4. Registrar venda do produto (O sistema deve receber o produto a ser vendido com o id e a quantidade. A quantidade vendida deve ser abatida do estoque. Se a quantidade de produtos a serem vendidos for maior que a quantidade no estoque, uma exceção deve ser lançada e uma mensagem informada ao usuário).
# 5. Sair

# Os dados dos produtos devem ser armazenados em arquivo texto, ou seja,
# ao sair do programa e iniciar de novo os dados não podem ser perdidos.
# Se houver inclusão de um produto existente, a quantidade deve ser incrementada. Lembrem-se de tratar as exceções.

import random

while True:
    print('Menu: ')
    print('1 - Incluir um produto')
    print('2 - Listar produtos')
    print('3 - Buscar produto')
    print('4 - Registrar venda')
    print('5 - Sair')
    opcao = int(input('Escolha uma opção: '))
    
    match opcao:
        case 1:
            # Incluir produto
            with open('Execicios-Python/questão68/produtos.txt', 'a') as produtos:
                nome = input('Nome do produto: ')
                try:
                    quantidade = int(input('Quantidade do produto: '))
                    valor_compra = float(input('Valor de compra: '))
                except ValueError:
                    print('Valor de compra inválido')
                    continue
                preco_venda = valor_compra + (valor_compra * 0.1)
                while True:
                    id = str(random.randint(0, 1000))
                    with open('Execicios-Python/questão68/ids.txt', 'r') as file:
                        ids = file.read().split('\n')
                        if id in ids:
                            continue
                        else:
                            with open('Execicios-Python/questão68/ids.txt', 'a') as f:
                                f.write(str(id) + '\n')
                                break
                    
                produtos.write(f'{id}, {nome}, {quantidade}, {valor_compra}, {preco_venda} \n')
                   
        case 2:
            # Listar produtos no estoque
            with open('Execicios-Python/questão68/produtos.txt', 'r') as produtos:
                print('Produtos cadastrados: ')
                for line in produtos:
                    print(line.split(',')[1])
        case 3:
            # Buscar produto por nome
            nome = input('Digite o nome do produto: ')
            with open('Execicios-Python/questão68/produtos.txt', 'r') as produtos:
                for line in produtos:
                    if nome.lower() in line.lower():
                        print(line)
                        break
                else:
                    print('Produto não encontrado')
        case 4:
            # Registrar venda do produto
            id = input('Digite o ID do produto: ')
            nome = input('Nome do produto: ')
            quantidade_vendida = int(input('Digite a quantidade vendida: '))
            
            with open('Execicios-Python/questão68/produtos.txt', 'r+') as produtos:
                linhas = produtos.readlines()
            
            with open('Execicios-Python/questão68/produtos.txt', 'w') as produtos:
                for line in linhas:
                    if line.split(',')[0] == id:
                        quantidade_atual = int(line.split(',')[2])
                        if quantidade_atual >= quantidade_vendida:
                            nova_quantidade = quantidade_atual - quantidade_vendida
                            line = f'{id}, {line.split(",")[1]}, {nova_quantidade}, {line.split(",")[3]}, {line.split(",")[4]}'
                            print(f'Venda realizada com sucesso! Novo estoque: {nova_quantidade}')
                        else:
                            print(f'Não há {quantidade_vendida} unidades do produto {nome} no estoque')
                            
                    produtos.write(line)
                    
        case 5:
            break
        case _:
            print('Opção inválida')