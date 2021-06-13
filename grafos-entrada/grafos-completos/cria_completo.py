def cria_matriz(vertices):
    matriz = []
    for i in range(vertices):
        linha = []
        for j in range(vertices):
            linha.append(" ")
        matriz.append(linha)
    return matriz
    
def adjacency_micielsky( w, x):
        if (w == x):
            matrix_kn = cria_matriz(w)
            for i in range(w):
                for j in range(w):
                    if (i == j):
                        matrix_kn[i][j] = 0
                    else:
                        matrix_kn[i][j] = 1
            return matrix_kn   
M = adjacency_micielsky(10, 10)

for i in M:
    print(i)
