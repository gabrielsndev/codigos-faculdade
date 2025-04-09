#Crie uma função multiplicar_listas(lista1, lista2) que recebe duas listas de números como strings e retorna uma nova lista contendo a multiplicação dos valores correspondentes.
#Se os tamanhos das listas forem diferentes ou houver um valor inválido, retorne "Erro: Listas incompatíveis".

def multiplicar_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        return 'Erro: Listas incompatíveis'

    resultado = []
    for i in range(len(lista1)):
        try:
            num1 = int(lista1[i])
            num2 = int(lista2[i])
            resultado.append(num1 * num2)
        except ValueError:
            return 'Erro: Listas contém valores inválidos'

    return resultado

