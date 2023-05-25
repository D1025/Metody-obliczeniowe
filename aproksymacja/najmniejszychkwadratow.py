import math

def gauss_elim(A:list[list[float]], b:list[float]) -> list[float]:
    """Elimacja Gaussa z odejmowaniem wtórnym

    Args:
        A (list[list[float]]): macierz rownan
        b (list[float]): lista wynikow rownan

    Raises:
        ValueError: gdy nie mozna znaleźć odwrotności

    Returns:
        list[float]: liste rozwiazan kolejnych niewiadmowych
    """
    # partial pivoting
    print(A, b)
    n = len(A)
    for i in range(n):
        max_row = max(range(i, n), key=lambda j: abs(A[j][i]))
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        # if abs(A[i][i]) < 1e-12:
        #     raise ValueError("Singular matrix")
        for j in range(i+1, n):
            # print(f"********FAKTOR:{A[j][i]}/{A[i][i]}*********")
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


def mnk(punkty:list[float], stopien:int, x:float) -> float:
    """Aproksymacja za pomocą metody najmniejszych kwadratów

    Args:
        punkty (list): list of a sets as (x, y) for points
        stopien (int): sets how accurate will be funcion
        x (float): point for aproksymation

    Returns:
        float: aproksymacja
    """
    Skj = []
    suma = 0
    #Suma wzorow Skj
    for potega in range(stopien*2+1):
        for punkt in punkty:
            suma+=punkt[0]**potega
        Skj.append(suma)
        suma = 0
    # print(f"Suma: {Skj}")
    #Suma wzororw Tk
    Tk = []
    for potega in range(stopien+1):
        for punkt in punkty:
            suma+=(punkt[0]**potega)*punkt[1]
            #print(f"{punkt[0]}**{potega}*{punkt[1]}")
        Tk.append(suma)
        suma = 0
        
        
    UkladSkj = []
    for i in range(potega+1):
        UkladSkj.append([])
        for j in range(potega+1):
            UkladSkj[i].append(Skj[i+j])
            
    wielomian = gauss_elim(UkladSkj, Tk)
    wynik = 0
    for w in enumerate(wielomian):
        wynik+=w[1]*(x**w[0])
        
    return wynik

punkty = []
for i in range(-10, 11, 5):
    x = i / 10.0
    punkty.append((x, math.sqrt(x**3 - 2*x + 2)))
    
    
#print(punkty)
# print(mnk([(1, 6), (2, 19), (3,40), (4,69)], 2, 2))
# print(mnk([(1, 6), (2, 19), (3,40), (4,69)], 2, 2.5))
print(mnk(punkty, 2, 0.25))
# print(mnk(punkty, 3, 0.25))
# print(mnk(punkty, 4, 0.25))
# print(mnk(punkty, 5, 0.25))
# print(mnk(punkty, 6, 0.25))


