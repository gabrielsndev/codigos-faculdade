import random
import string 

def gerar_senha(tipo, tamanho):
    if tipo == '1':
        stringue = string.ascii_letters + string.punctuation
        senha = ''
        for i in range(tamanho):
            senha += random.choice(stringue)
        return senha
    
    elif tipo == '2':
        stringue = string.digits
        senha = ''
        for i in range(tamanho):
            senha += random.choice(stringue)

        return senha

    else:
        stringue = string.ascii_letters + string.digits
        senha = ''
        for i in range(tamanho):
            senha += random.choice(stringue)
        return senha 

