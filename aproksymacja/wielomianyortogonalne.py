import math


def simpson(funcion, _a, _b, n):
    xi = [_a]
    ti = []
    for i in range(1, n):
        xi.append(_a+(i/n)*(_b-_a))
    xi.append(_b)
    for i in range(0, len(xi)-1):
        ti.append((xi[i+1]+xi[i])/2)    
    h = (xi[1]-xi[0])/2
    wynik = h/3
    dodawanie=0
    for i in range(0, n):
        dodawanie+=funcion(xi[i])+4*funcion(ti[i])+funcion(xi[i+1])
    wynik*=dodawanie
    return wynik


def fi(x, n):
    if n == 1:
        return x
    if n == 0:
        return 1
    return (1/n)*(2*n-1)*x*fi(x, n-1)-((n-1)/n)*fi(x, n-2)


def Ci(n, px, a, b, funkcja):
    wzor = lambda x, n=n: px(x) * fi(x, n) * funkcja(x)
    return (1/li(n, px, a, b))*simpson(wzor, a, b, 16)
    
def li(n, px, a, b):
    wzor = lambda x, n=n: px(x)*(fi(x,n)**2)
    return simpson(wzor, a, b, 16)

def g(x, n, px, a, b, funkcja):
    g = 0
    for i in range(n):
        g+=Ci(i, px, a, b, funkcja)*fi(x, i)
    return g


print(g(0.25, 16, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))

# print(li(1, lambda x: 1, -1, 1))
        
    
    

