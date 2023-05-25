from warunek import warunek


def bisekcja(a:float, b:float, f, epsilon:float) -> float:
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
        return x
    else:
        if f(a) < 0:
            if f(x) < 0:
                return bisekcja(x, b, f, epsilon)
            else:
                return bisekcja(a, x, f, epsilon)
        else:
            if f(x) < 0:
                return bisekcja(a, x, f, epsilon)
            else:
                return bisekcja(x, b, f, epsilon)
            
            
print(bisekcja(-10, -3, lambda x: x**2+4.1*x -9, 0.05))
print(bisekcja(-4, -2, lambda x: 6*x**2+13*x -5, 0.05))
