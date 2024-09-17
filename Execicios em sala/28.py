#a) Uma função que receba uma string e retorne a string criptografada. O método de criptografia
#será baseado na seguinte regra: trocar alguns caracteres por outros, conforme a tabela abaixo:
#
#b) Um programa que leia uma frase e exiba na tela o conteúdo do arquivo lido criptografado (use
#a função definida no item anterior para fazer a criptografia).
def descrip(ff):
    c = ''
    for x in ff:
        if x == "@":
            x = "a"
            c += x
        
        elif x == "3":
            x = "e"
            c += x

        elif x == "!":
            x = "i"
            c += x

        else:
            c += x
    return(c)           

def crip (ff):
    c = ""
    for x in ff:
        if x == 'a':
            x = '@'
            c += x

        elif x == 'e':
            x = '3'
            c += x
        
        elif x == 'i':
            x = '!'
            c += x

        else:
            c += x
    return (c)


f = input("Digite uma frase: ")

print (f"Sua frase Crip: {crip(f)}")
print (f"Sua frase DesCrip: {descrip(f)}")

        
        