import math

def f1(x):
    return x*x

def moja(x):
    return (x*x+5.2)/(math.sin(0.5+0.1*x*x))

def f2(x):
    return (x*x*math.sqrt(1+x))/(1+x*x)

def trapez(funcion, _a, _b, n):
    h = (_b - _a)/n
    punkty = []
    for i in range(1, n):
        punkty.append(_a+(i/n)*(_b-_a))
    
    wynik = ((funcion(_a)+funcion(punkty[0]))/2)*h
    for i in range(0, len(punkty)-1):
        wynik+=((funcion(punkty[i])+funcion(punkty[i+1]))/2)*h
    wynik+=((funcion(punkty[len(punkty)-1])+funcion(_b))/2)*h
    
    return wynik


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
    
    
    
    

# print(trapez(f1, 1, 4, 3))
# print(simpson(f1,1, 4, 3))
# print(simpson(f2, 0, 2, 3))

print("////////////////////////////")
print("----------TRAPEZ----------")
print("n=2",trapez(moja, 1, 4, 2))
print("n=4",trapez(moja, 1, 4, 4))
print("n=6",trapez(moja, 1, 4, 6))
print("n=8",trapez(moja, 1, 4, 8))
print("n=10",trapez(moja, 1, 4, 10))
print("n=16",trapez(moja, 1, 4, 16))
print("----------SIMPSON----------")
print("n=2",simpson(moja, 1, 4, 2))
print("n=4",simpson(moja, 1, 4, 4))
print("n=6",simpson(moja, 1, 4, 6))
print("n=8",simpson(moja, 1, 4, 8))
print("n=10",simpson(moja, 1, 4, 10))
print("n=16",simpson(moja, 1, 4, 16))
print("////////////////////////////")

