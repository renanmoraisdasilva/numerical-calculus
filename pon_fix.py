import math

print("\nMÉTODO PONTO FIXO:\n")

contador = 0

# Implementing Fixed Point Iteration Method
def PontoFixo(f,g,p0,erro):
    
    global contador
    contador = 0
    pn = p0
    while True:
        g_p_n = g(pn)
        pn = g_p_n
        contador += 1
        if abs(f(g_p_n)) < erro:
            global f_x
            f_x = f(g_p_n)
            break
    
    return g_p_n

# criei uma função para printar para que o código tivesse menos prints
def print_resultados(n, raiz, f_x, contador):
    print(f"Exemplo {n}  :\nRaiz : " + str(raiz))
    print(f"f(x) : " + str(f_x))
    print("Número de iterações: " + str(contador))
    print("--------------------------------")

# exemplo 18

f = lambda x: math.exp(-x*x) - math.cos(x)
g = lambda x: math.cos(x) - math.exp(-x*x) + x
raiz_1 = PontoFixo(f,g,1.5,pow(10,-4))
print_resultados(18, raiz_1, f_x, contador)


# exemplo 19

f = lambda x: (x * x * x - x - 1)
g = lambda x: pow(x + 1, 1/3)
raiz_2 = PontoFixo(f,g,1,pow(10,-6))
print_resultados(19, raiz_2, f_x, contador)


# exemplo 20

f = lambda x: (4 * math.sin(x) - math.exp(x))
g = lambda x: x - 2 * math.sin(x) + 0.5 * math.exp(x)
raiz_3 = PontoFixo(f,g,0.5,pow(10,-5))
print_resultados(20, raiz_3, f_x, contador)


# exemplo 21
f = lambda x: x * math.log(x,10) - 1
g = lambda x: x - 1.3 * (x * math.log(x,10) - 1)
raiz_4 = PontoFixo(f,g,2.5,pow(10,-7))
print_resultados(21, raiz_4, f_x, contador)