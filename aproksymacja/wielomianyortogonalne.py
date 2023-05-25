import math


def simpson(funcion, _a:float, _b:float, n:int) -> float:
    """całka liczona na przedziale a-b liczona za pomocą metody Simpsona

    Args:
        funcion (function): funkcja całkowa
        _a (float): poczatek przedzialu
        _b (float): koniec przedzialy
        n (int): ilosc krokow

    Returns:
        float: calka
    """
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


def fi(x:float, n:int) ->float:
    """𝜑 n - wielomian Legendre'a   

    Args:
        x (float): punkt dla jakiego liczymy wielomian lagranda
        n (int): stopien wielomianu

    Returns:
        float: wielomian
    """
    if n == 1:
        return x
    if n == 0:
        return 1
    return (1/n)*(2*n-1)*x*fi(x, n-1)-((n-1)/n)*fi(x, n-2)


def Ci(n:int, px, a:float, b:float, funkcja) -> float:
    """stały współczynniki

    Args:
        n (int): punkt dokladnosci
        px (function): funkcja wagi
        a (float): poczatek przedzialu
        b (float): koniec przedzialy
        funkcja (function): funkcja dla ktorej wyznaczamy współczynnik Ci

    Returns:
        float: współczynnik Ci
    """
    wzor = lambda x, n=n: px(x) * fi(x, n) * funkcja(x)
    return (1/li(n, px, a, b))*simpson(wzor, a, b, 16)
    
def li(n:int, px, a:float, b:float) -> float:
    """lambda

    Args:
        n (int): punkt dokladnosci
        px (function): funkcja wagi
        a (float): poczatek przedzialu
        b (float): koniec przedzialu

    Returns:
        float: wynik lambdy
    """
    wzor = lambda x, n=n: px(x)*(fi(x,n)**2)
    return simpson(wzor, a, b, 16)

def g(x:float, n:int, px, a:float, b:float, funkcja) -> float:
    """Aproksymacja ZA POMOCĄ WIELOMIANÓW ORTOGONALNYCH

    Args:
        x (float): punkt do liczenia aproksymacji
        n (int): dokładność
        px (function): funkcja wagi
        a (float): poczatek przedzialu
        b (float): koniec przedzialu
        funkcja (function): funkcja dla ktorej wykonamy aproksymacje

    Returns:
        float: wynik aproksymacji
    """
    g = 0
    for i in range(n):
        g+=Ci(i, px, a, b, funkcja)*fi(x, i)
    return g


print(g(0.25, 2, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
print(g(0.25, 3, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
print(g(0.25, 4, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
print(g(0.25, 5, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
print(g(0.25, 6, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
# print(g(0.25, 10, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
# print(g(0.25, 14, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
# print(g(0.25, 18, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))
# print(g(0.25, 20, lambda x: 1, -1, 1, lambda x: math.sqrt(x**3-2*x+2)))




# print(li(1, lambda x: 1, -1, 1))
        
    
    

