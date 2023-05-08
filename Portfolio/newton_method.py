import numpy as np
import sympy as sym

# Criando 

def newton_method(func, funcderiv, x, n):

    def f(x):
        f = eval(func)
        return f
    
    def df(x):
        df = eval(funcderiv)
        return df
    
    for interacoes in range(1,n):
        i = x - (f(x) / df(x))
        x = i
    
    print(f"A raiz foi encontrada {x} apos {n} interaçoes")

newton_method("x**2 - 2", "2*x", 2, 10)
