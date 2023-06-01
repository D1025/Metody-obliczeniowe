from warunek import warunek


def bisekcja(a:float, b:float, f, epsilon:float, iteraje:int=0) -> float:
    """Metoda bisekcji dla równań nieliniowych

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
        raise Exception("Nie spełniony warunek konieczny")
    
    x = (a + b)/2
    if abs(f(x)) < epsilon:
        return x, iteraje
    else:
        if f(a) < 0:
            if f(x) < 0:
                return bisekcja(x, b, f, epsilon, iteraje+1)
            else:
                return bisekcja(a, x, f, epsilon, iteraje+1)
        else:
            if f(x) < 0:
                return bisekcja(a, x, f, epsilon, iteraje+1)
            else:
                return bisekcja(x, b, f, epsilon, iteraje+1)
            
            
print(bisekcja(-10, -3, lambda x: x**2+4.1*x -9, 0.1))
print(bisekcja(-10, -3, lambda x: x**2+4.1*x -9, 0.05))
print(bisekcja(-10, -3, lambda x: x**2+4.1*x -9, 0.01))
print(bisekcja(-10, -3, lambda x: x**2+4.1*x -9, 0.005))
print(bisekcja(-10, -3, lambda x: x**2+4.1*x -9, 0.001))



