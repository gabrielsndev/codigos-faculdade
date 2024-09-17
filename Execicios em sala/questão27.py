def kk (m, k):
    cont = 0
    for l in range(nlin):
        for c in range(ncol):
         if m[l][c] == k:
            cont += 1

    return  (f"O valor {k} apareceu {cont} vezes")


k = int(input("k: "))
ncol = 2
nlin = 3

mat = [None]*nlin

for x in range(nlin):
    mat[x] = [None]*ncol

for l in range(nlin):
    for c in range(ncol):
         mat[l][c] = int(input("Digite um valor: "))

print (mat)

print(kk(mat,k))


