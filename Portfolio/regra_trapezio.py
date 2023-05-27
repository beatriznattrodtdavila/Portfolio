# Regra do Trapezio

# Definir função para integrar
def f(x):
    return 1/(1 + x**2)

# Regra do trapezio
def trapezoidal(x0,xn,n):
    h = (xn - x0) / n
    
    # Encontrando soma 
    integracao = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integracao = integracao + 2 * f(k)
    
    integracao = integracao * h/2
    
    return integracao
    

inf_limite = float(input("Limite fe integração inferior: "))
sup_limite = float(input("Limite de integração superior: "))
sub_intervalo = int(input("ENúmero de subintervalos: "))


resulto = trapezoidal(inf_limite, sup_limite, sub_intervalo)
print("O resultado da integração pela regra do trapezio é: %0.6f" % (resulto) )