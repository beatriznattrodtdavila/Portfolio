#importando library
import numpy as np
import sys

# Tamanho da matriz
n = int(input('Sendo n x n o tamanho da matriz, digite o valor de n: '))
print(n)

# Criando um array para guardar os elementos da matrix
# Esse array vai é de n x (n + 1)
# Este array se inicia com valores 0
A = np.zeros((n, n + 1))

# Criando um array para guardar a solução
# Este array se inicia com valores 0
x = np.zeros(n)

# Elementos da matriz
# i = linhas ; j = colunas
for i in range(n):
    for j in range(n + 1):
        print("Insira os elementos da Matriz" )
        A[i][j] = float(input ( "A[" + str(i) + "][" + str(j) + "] = "))

A_copia = A.copy()

for i in range(n):
    if A[i][i] == 0.0:
        sys.exit('Divisão por zero detectada!')
        # Eliminação de Gauss
    for j in range(i + 1, n):
        multiplicador = A[j][i] / A[i][i]
        for k in range(n + 1):
            A[j][k] = A[j][k] - multiplicador * A[i][k]



x[n - 1] = A[n - 1][n] / A[n - 1][n-1]

for i in range(n - 2, -1, -1):
    x[i] = A[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - A[i][j] * x[j]

    x[i] = x[i] / A[i][i]


#Printando o resultado

print(" Matriz Inicial: ")
print(A_copia)
print("\n \n Matriz Escalonada: ")
print(A)
print("\n \n O resultado é: \n")
for i in range(n):
    print('X%d = %0.2f' %(i, x[i]), end = '\t')
print("\n")
