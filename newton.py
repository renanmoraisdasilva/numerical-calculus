import math

print("\nMÉTODO NEWTON:\n")

contador = 0

def newton(f,df,x0,erro):

    global contador
    contador = 0
    
    xn = x0
    
    while True:
        xn = xn - f(xn)/df(xn)
        contador += 1
        if abs(f(xn)) < erro:
            global f_x
            f_x = f(xn)
            break
        
        if df(xn) == 0:
            print('Derivada zero.')
            return None

    return xn
    
# criei uma função para printar para que o código tivesse menos prints
def print_resultados(n, raiz, f_x, contador):
    print(f"Exemplo {n}  :\nRaiz : " + str(raiz))
    print(f"f(x) : " + str(f_x))
    print("Número de iterações: " + str(contador))
    print("--------------------------------")


# exemplo 18

f = lambda x: math.exp(-x*x) - math.cos(x)
df = lambda x: math.sin(x) - 2 * x * math.exp(-x*x)
raiz_1 = newton(f,df,1.5,pow(10,-4))
print_resultados(18, raiz_1, (f_x),contador)


# exemplo 19

f = lambda x: (x * x * x - x - 1)
df = lambda x: 3 * pow(x,2) - 1
raiz_2 = newton(f,df,0,pow(10,-6))
print_resultados(19, raiz_2, (f_x), contador)


# exemplo 20

f = lambda x: 4 * math.sin(x) - math.exp(x)
df = lambda x: 4 * math.cos(x) - math.exp(x)
raiz_3 = newton(f,df,0.5,pow(10,-5))
print_resultados(20, raiz_3, (f_x), contador)

# exemplo 21

f = lambda x: (x * math.log(x,10) - 1)
df = lambda x: (math.log(x,10) + 1/math.log(10))
raiz_4 = newton(f,df,2.5,pow(10,-7))
print_resultados(21, raiz_4, (f_x), contador)