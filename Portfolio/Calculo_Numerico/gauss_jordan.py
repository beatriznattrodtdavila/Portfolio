import numpy as np

def gauss_jordan(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    
    for k in range(n):
        # Pivo Parcial
        # Checar se o 1 elemento da matriz é 0 ou bem proximo de 0
        if np.fabs(a[k,k]) < 1.0e-18:
        # Caso a afirmação acima seja verdadeira verificar se os elementos abaixo do 1, ou seja, os elementos da mesma coluna, porem das outras linhas for maior em valor absoluto que o 1 elemento temos que trocar as linhas de lugar
            for i in range(k + 1, n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k,n):
                        a[k,j], a[i,j] = a[i,j], a[k,j]
                    b[k], b[i] = b[i], b[k]
                    break
        # Dividindo os todos os elementos da linha do pivo pelo pivo
        pivot = a[k,k]
        for j in range(k,n):
            a[k,j] /= pivot
        b[k] /= pivot
        # Eliminação
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            fator = a[i,k]
            for j in range(k,n):
                a[i,j] -= fator * a[k,j]
            b[i] -= fator * b[k]
    return b, a

a = [[0,2,0, 1], [2,2,3,2], [4,-3,0,1], [6,1,-6,-5]]
b = [0,-2,-7,6]

X, A = gauss_jordan(a,b)
print("A solução do sistema é: ", X)
print("A matriz transformada será: \n", A)