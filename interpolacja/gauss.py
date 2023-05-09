import numpy as np


def gaussian_elimination(A, b):
    """
    Funkcja ta rozwiązuje układ równań liniowych Ax = b
    za pomocą eliminacji Gaussa z częściowym wyborem elementów głównych.
    A - macierz współczynników
    b - wektor wyrazów wolnych
    """

    n = len(A)

    # Krok 1: eliminacja współczynników
    for i in range(n):
        # Wyszukaj wiersz z maksymalną wartością bezwzględną w kolumnie i
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j

        # Zamień wiersze i i max_row
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Wykonaj eliminację Gaussa w kolumnie i
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i+1, n):
                A[j][k] -= factor * A[i][k]
            b[j] = np.array(b[j]) - factor * np.array(b[i])
            A[j][i] = 0

    # Krok 2: wyliczenie rozwiązania
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


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
