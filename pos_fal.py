import math

print("\nMÉTODO POSIÇÃO FALSA:\n")

contador = 0

def PosiçãoFalsa(f,a,b,erro):

    if f(a) * f(b) >= 0:
        print("Método falhou.")
        return None
        
    global contador
    contador = 0
    
    a_n = a
    b_n = b
    
    while True:
        p_n = ( a_n * f(b_n) - b_n * f(a_n) )/( f(b_n) - f(a_n) )
        
        contador += 1
        
        if abs(f(p_n)) < erro:
            global f_x
            f_x = f(p_n)
            break
        
        if f(a_n) * f(p_n) < 0:
            b_n = p_n
        elif f(b_n) * f(p_n) < 0:
            a_n = p_n

    return p_n

# criei uma função para printar para que o código tivesse menos prints
def print_resultados(n, raiz, f_x, contador):
    print(f"Exemplo {n}  :\nRaiz : " + str(raiz))
    print(f"f(x) : " + str(f_x))
    print("Número de iterações: " + str(contador))
    print("--------------------------------")


# exemplo 18

f = lambda x: math.exp(-x*x) - math.cos(x)
raiz_1 = PosiçãoFalsa(f,1,2,pow(10,-4))
print_resultados(18, raiz_1, f_x, contador)

# exemplo 19

f = lambda x: (x * x * x - x - 1)
raiz_2 = PosiçãoFalsa(f,1,2,pow(10,-6))
print_resultados(19, raiz_2, f_x, contador)

# exemplo 20

f = lambda x: (4 * math.sin(x) - math.exp(x))
raiz_3 = PosiçãoFalsa(f,0,1,pow(10,-5))
print_resultados(20, raiz_3, f_x, contador)

# exemplo 21

f = lambda x: (x * math.log(x,10) - 1)
raiz_4 = PosiçãoFalsa(f,2,3,pow(10,-7))
print_resultados(21, raiz_4, f_x, contador)