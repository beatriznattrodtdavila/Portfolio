import numpy as np

# Sabendo que: x^(k+1) = (b - (L + U)*x) / D
# D = A[i][i]
# L = matriz diagonal inferior de A
# U = matriz diagonal superior de A

def jacobi(A, b):
    interacao = 1000

# Escrevendo o sistema
    print("Sistema:")
    for i in range(A.shape[0]):
            linha = [f"{A[i, j]}*x{j + 1}" for j in range(A.shape[1])]
            print(f'{" + ".join(linha)} = {b[i]}')
    print()

# Criando um chute inicial x; Criando um loop para mostrar o numero da interação e seu respectivo valor da solução para x; Criando uma variavel x_novo que ira abrigar os valores do x a cada nova interação
    x = np.zeros_like(b)
    for contagem_interacao in range(1, interacao):
        print(f"Iteração {contagem_interacao}: {x}")
        x_novo = np.zeros_like(x)

# Aplicando a formula
        for i in range(A.shape[0]):
            # matriz triangular inferior
            s1 = np.dot(A[i, :i], x[:i])
            # matriz triangular superior
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_novo[i] = (b[i] - s1 - s2) / A[i, i]
            # Se o x_novo por igual ao anterior parar o loop
            if x_novo[i] == x_novo[i-1]:
              break

# Retorna True se dois arrays forem iguais em elementos dentro de uma tolerância.
# Se forem diferentes o sistema volta a fazer o loop de aplicar a formula, encontrar um x_novo e realizar a checagem de tolerancia novamente
        if np.allclose(x, x_novo, atol=1e-10, rtol=0.):
            break

        x = x_novo

    print("Solução: ")
    print(x)
    erro = np.dot(A, x) - b
    print("Erro:")
    print(erro)

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])

b = np.array([6., 25., -11., 15.])


jacobi(A,b)
