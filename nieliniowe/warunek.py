def warunek(a:float, b:float, f) -> bool:
    """Warunek konieczny

    Args:
        a (float): poczatek przedzialu
        b (float): koniec przedzialu
        f (funcion): funkcja

    Returns:
        bool: zwraca czy w przedziale istnieje miejsce zerowe
    """
    return f(a)*f(b)<0


def d_fun(f, x:float) -> float:
    """pochodna z definicji po funkcji f dla punktu x
    """
    h = 1e-5
    return (f(x+h)-f(x-h))/(2*h)

def d_fun_2(f, x:float) -> float:
    """pochodna drugiego stopnia z definicji po funkcji f dla punktu x
    """
    h = 1e-5
    return (d_fun(f,x+h)-d_fun(f,x-h))/(2*h)
