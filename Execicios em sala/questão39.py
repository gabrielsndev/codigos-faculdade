# Crie um programa que receba o nome, a idade de uma pessoa e adicione esses dados em um dicionário.
# Depois crie uma nova chave com valor booleano, infomando se o aluno é de maior(True) ou não (False)

dicionario = {
    'nome': input('Digite o nome: '),
    'idade': int(input('Digite a idade: '))
}

dicionario['maior_idade'] = dicionario['idade'] >= 18

print(dicionario)