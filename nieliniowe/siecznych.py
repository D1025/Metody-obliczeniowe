from warunek import warunek, d_fun


def Xnplus1_b(f, x0:float, b:float) -> float:
    return x0-(f(x0)/(f(b)-f(x0)))*(b-x0)

def Xnplus1_a(f, x0:float, a:float) -> float:
    return x0-(f(x0)/(f(x0)-f(a)))*(x0-a)
    
def siecznych_a(a:float, x0:float, f, epsilon:float, interacje:int) -> float:
    x1 = Xnplus1_a(f, x0, a)
    if abs(f(x1)) < epsilon:
        return x1, interacje
    return siecznych_a(a, x1, f, epsilon, interacje+1)

def siecznych_b(x0:float, b:float, f, epsilon:float, interacje:int) -> float:
    x1 = Xnplus1_b(f, x0, b)
    if abs(f(x1)) < epsilon:
        return x1, interacje
    return siecznych_b(x1, b, f, epsilon, interacje+1)


def siecznych(a:float, b:float, f, epsilon:float) -> float:
    """Metoda siecznych dla równań nieliniowych

    Args:
        a (float): poczatek przedzialu
        b (float): koniec przedzialu
        f (function): fukcja
        epsilon (float): odchylenie
        
    Raises:
        Exception: gdy nie zostanie spełniowy warunek koenieczny
        
    Returns:
        float: argument dla bliski rób równy miejsca zerowego dla funkcji
    """
    if not warunek(a, b, f):
        raise Exception("Niepoprawny warunek początkowy")
    
    iteracje = 1
    if (f(a)>0 and d_fun(f, a)>0) or (f(a) < 0 and d_fun(f, a) < 0):
        return siecznych_a(a, b, f, epsilon, iteracje)
    else:
        return siecznych_b(a, b, f, epsilon, iteracje)
        
    
        
print(siecznych(-10, -3, lambda x: x**2+4.1*x -9, 0.1))
print(siecznych(-10, -3, lambda x: x**2+4.1*x -9, 0.05))
print(siecznych(-10, -3, lambda x: x**2+4.1*x -9, 0.01))
print(siecznych(-10, -3, lambda x: x**2+4.1*x -9, 0.005))
print(siecznych(-10, -3, lambda x: x**2+4.1*x -9, 0.001))
