with open('texto1.txt', 'r') as f:
    texto1 = f.read()

with open('texto2.txt', 'w') as file:
    file.write(texto1)