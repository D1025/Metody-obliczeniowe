ZADANIE = [(-4.0, -116.0), (-2.0, -20.0), (0.0,4.0), (2.0,4.0), (4.0,28.0)]

def validation(x, y):
        x1 = float(x)
        y1 = float(y)
        return x1, y1
    
    
    
def wierd_pi(i, x):
    j = 0
    iloraz = 1
    for points in ZADANIE:
        if j==i:
            j+=1
            continue
        iloraz *= (x-points[0])/(ZADANIE[i][0]-points[0])
        j+=1
    return iloraz
        

    
    
def interpolation(x):
    i = 0
    suma = 0
    for points in ZADANIE:
        suma+=points[1]*wierd_pi(i, x)
        i+=1
    return suma

print(interpolation(1))
