from warunek import warunek, d_fun, d_fun_2


def Xnplus1(f, x:float) -> float:
    """Argument następny dla metody statycznej
    """
    return x - f(x)/d_fun(f, x)

def interuj(f, x0:float, epsilon:float, iteracje:int) -> float:
    x1 = Xnplus1(f, x0)
    if abs(f(x1))<epsilon or abs(x1-x0) < epsilon:
        return x1, iteracje
    return interuj(f, x1, epsilon, iteracje+1)
    


def statycznych(a:float, b:float, f, epsilon:float) -> float:
    """metoda statyczna dla równań nieliniowych

    Args:
        a (float): poczatek przedzialu
        b (float): koniec przedzialu
        f (function): fukcja
        epsilon (float): odchylenie

    Returns:
        float: argument dla bliski rób równy miejsca zerowego dla funkcji
    """
    if warunek(a, b, f):
        print("Poprawny warunek początkowy")
    else:
        print("Niepoprawny warunek początkowy")
    if d_fun(f, a)*d_fun(f, b)>=0 and d_fun_2(f, a)*d_fun_2(f, b)>=0:
        print("warunki zbieżności są spełnione")
    else:
        print("warunki zbieżności nie są spełnione")
        
    if d_fun_2(f, a)*f(a) >=0:
        x0 = a
    else:
        x0 = b
    iteracje = 1
    return interuj(f, x0, epsilon, iteracje)
    
    
print(statycznych(-10, -3, lambda x: x**2+4.1*x -9, 0.1))
print(statycznych(-10, -3, lambda x: x**2+4.1*x -9, 0.05))
print(statycznych(-10, -3, lambda x: x**2+4.1*x -9, 0.01))
print(statycznych(-10, -3, lambda x: x**2+4.1*x -9, 0.005))
print(statycznych(-10, -3, lambda x: x**2+4.1*x -9, 0.001))

    
    
    