# Simpson's 1/3

# Definir a função para integrar
def f(x):
    return x**2

# Função Simpson 1/3 
def simpson13(x0,xn,n):
    h = (xn - x0) / n
    
    # Encontrando a soma
    integracao = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integracao = integracao + 2 * f(k)
        else:
            integracao = integracao + 4 * f(k)
    

    integracao = integracao * h/3
    
    return integracao
    

inf_limite = float(input("Limite fe integração inferior: "))
sup_limite = float(input("Limite de integração superior: "))
sub_intervalo = int(input("Número de subintervalos: "))


resulto = simpson13(inf_limite, sup_limite, sub_intervalo)
print("O resultado da integração pelo método Simpson's 1/3 é: %0.6f" % (resulto) )