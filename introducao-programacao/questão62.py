#Crie uma função buscar_palavra(lista, palavra) que recebe uma lista de palavras e verifica se a palavra está presente.
#Se estiver, retorne o índice. Se não estiver, retorne "Palavra não encontrada". Se a entrada não for uma lista, capture a exceção e retorne "Entrada inválida".

def buscar_palavras(lista, palavra):
    if type(lista) == list():
        return 'Entrada inválida'

    if palavra in lista: 
        return f'A palavra está na lista, no index: {lista.index(palavra)}'

    else: return 'Palavra não encontrada'


lista = ['Python', 'is', 'awesome', 'and', 'fun']
palavra_teste = 'awesome'

print(buscar_palavras(lista, palavra_teste))
print(buscar_palavras(['Python', 123, 'is', 'awesome'], palavra_teste)) 

