lista_geral = []
dicionario = {}
with open('transacoes.csv', 'r') as arquivo:
    conteudo = arquivo.readlines()
    soma_de_tudo = 0
    for linha in conteudo:
        linha = linha.strip()
        lista = list(linha.split(';'))
        lista_geral.append(lista)
        try:
            novo_valor = lista[-1].replace('.','')
            novo_valor = novo_valor.replace(',','.')
            valor = float(novo_valor)
            if lista[2] not in dicionario:
                dicionario[lista[2]] = valor
            else:
                dicionario[lista[2]] += valor
            soma_de_tudo += valor
        except:
            pass

with open('novo-arquivo.csv', 'x') as novo_arquivo:
    for key, valor in dicionario.items():
        novo_arquivo.write(f'{key};{valor}\n')