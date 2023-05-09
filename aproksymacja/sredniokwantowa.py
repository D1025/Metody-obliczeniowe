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

def gauss_elim(A, b):
    # partial pivoting
    n = len(A)
    for i in range(n):
        max_row = max(range(i, n), key=lambda j: abs(A[j][i]))
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        if abs(A[i][i]) < 1e-12:
            raise ValueError("Singular matrix")
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j][i] = 0
            for k in range(i+1, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # back substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def ciagla(a:int, b:int, x:int, p:int, n:int, f) -> float:
    """_summary_

    Args:
        a (int): Początek przedzialy
        b (int): koniec przedziału
        x (int): punkt
        p (int): waga
        n (int): stopien poszukiwanego wielomianu
        f (function): fukcja dla ktorej szukamy aproksymacji

    Returns:
        float: aproksymacja sredniokwadratowa (ciagla)
    """
    Aij = [[]]
    bi = []
    for i in range(0, n+1):
        for j in range(0, n+1):
            Aij[i].append(simpson(lambda x:(x**i)*(x**j)*p, a, b, 16))
        if i!=n:
            Aij.append([])
    for i in range(0, n+1):
        bi.append(simpson(lambda x:(x**i)*f(x)*p, a, b, 16))
    
    g = gauss_elim(Aij, bi)
    wynik = 0
    for i in range(len(g)):
        wynik+=g[i]*(x**i)
        
    return wynik

print(ciagla(1, 3, 1, 1, 2, lambda x: math.sqrt(x)))
print(ciagla(1, 3, 2, 1, 2, lambda x: math.sqrt(x)))
print(ciagla(-1, 1, 0.25, 1, 2, lambda x: math.sqrt(x**3-2*x+2)))


    