from gauss import gauss_elim

def power(x, p):
    w=x
    for i in range(p):
        w*=x 
    return w

ZADANIE = [(-4.0, -116.0), (-2.0, -20.0), (0.0,4.0), (2.0,4.0), (4.0,28.0)]
TABELKA = []
WYNIKI = []
POCHODNE = [(-4.0, 74.0), (4.0,26.0)]
X = 1

LENGHT = len(ZADANIE)
for i in range(LENGHT+2):
    TABELKA.append([])
    for j in range(LENGHT+2):
        TABELKA[i].append(0.0)
        
        
# print(TABELKA)


for i in range(LENGHT):
    TABELKA[i][0]=1.0
    TABELKA[i][1]=ZADANIE[i][0]
    TABELKA[i][2]=ZADANIE[i][0]*ZADANIE[i][0]
    TABELKA[i][3]=ZADANIE[i][0]*ZADANIE[i][0]*ZADANIE[i][0]

    for j in range(1,i):
        TABELKA[i][3+j]=power(ZADANIE[i][0]-ZADANIE[j][0], 3)
    WYNIKI.append(ZADANIE[i][1])
    
for i in range(LENGHT,LENGHT+2):
    TABELKA[i][0]=0.0
    TABELKA[i][1]=1.0
    TABELKA[i][2]=2*POCHODNE[i-LENGHT][0]
    TABELKA[i][3]=3*POCHODNE[i-LENGHT][0]*POCHODNE[i-LENGHT][0]
    
    for j in range(3):
        TABELKA[i][4+j]=3*(power(POCHODNE[i-LENGHT][0]-ZADANIE[j][0], 3))
    WYNIKI.append(POCHODNE[i-LENGHT][1])
    
# print(TABELKA)
    

    
# Example usage
solutions = gauss_elim(TABELKA, WYNIKI)
print(solutions)
w=0
w+=solutions[0]+solutions[1]*X+solutions[2]*X*X+solutions[3]*X*X*X
for i in range(1,LENGHT-1):
   if X>ZADANIE[i][0]:
       w+= solutions[i+3]*(power(X-ZADANIE[i][0],3))

# print(TABELKA)
# w += solutions[1+3]*(power(X-ZADANIE[1][0],3))+solutions[2+3]*(power(X-ZADANIE[2][0],3))

print(w)
    


