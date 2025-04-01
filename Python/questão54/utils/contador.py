def contador(frase):
    letras = {}  
    for letra in frase:
        if letra != ' ':
            if letra in letras:
                letras[letra] += 1
            else:
                letras[letra] = 1
    return letras
