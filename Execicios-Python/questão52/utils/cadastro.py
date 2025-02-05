def cadastrar(produto, preco, lista):
    produto = {'nome': produto, 'preço': preco}
    lista.append(produto)
    return lista

def aumentar(lista, produto, percentual):
    percentual = percentual / 100
    for i in lista:
        if i['nome'] == produto:
            valor = i['preço']
            porcentagem = valor * percentual
            i['preço'] = valor + porcentagem
    return lista