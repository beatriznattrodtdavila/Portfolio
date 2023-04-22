def escalonamento(A, b):
    n = len(b) # n tem o tamanho de b
    x = [0] * n # n elementos no array x de valor 0

    # Calculo dos pivores
    for k in list(range(1,n, 1)):
        # Calculo dos multiplicadores para cada linha que modifico
        for i in list(range(k+1, n + 1, 1)):
            m = A[i - 1][k - 1] / A[k - 1][k - 1]
            A[i - 1][k - 1] = 0
            b[i - 1] = b[i - 1] - m*b[k - 1]
            #Atualizar demais valores da linha
            for j in list(range(k + 1, n + 1, 1)):
                A[i - 1][j - 1] = A[i - 1][j - 1] - m*A[k - 1][j - 1]

    return A, b


def resolucao_triangular_superior(U,b):
    n = len(b) # n tem o tamanho de b
    x = [0] * n # n elementos no array x de valor 0
    x[n - 1] = b[n - 1] / U[n - 1][n - 1]

    for i in list(range(n - 1, 0, -1)):
        s = 0
        for j in list(range(i + 1, n + 1, 1)):
            s = s + U[i - 1][j - 1] * x[j - 1]
        
        x[i - 1] = (b[i - 1] - s) / (U[i - 1][i - 1])

    return x



# Teste com dados
Ai = [[1,1,1],
     [2,1,-2],
     [2,2,1]]

bi = [1,0,1]

# Transformando em sistema equivalente
U,b = escalonamento(Ai,bi) # U = matriz triangular superior, b transformado
print("U = ", U)
print('b = ', b)
x = resolucao_triangular_superior(U,b)
print("x = ", x)