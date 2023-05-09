import tkinter as tk

PUNKTY = []
ZADANIE = [(-4.0, -116.0), (-2.0, -20.0), (0.0,4.0), (2.0,4.0), (4.0,28.0)]

def validation(x, y):
        x1 = float(x)
        y1 = float(y)
        return x1, y1
    
    
    
def wierd_pi(i, x):
    j = 0
    iloraz = 1
    for points in PUNKTY:
        if j==i:
            j+=1
            continue
        iloraz *= (x-points[0])/(PUNKTY[i][0]-points[0])
        j+=1
    return iloraz
        

    
    
def interpolation(x):
    i = 0
    suma = 0
    for points in PUNKTY:
        suma+=points[1]*wierd_pi(i, x)
        i+=1
    return suma




def button1_clicked():
    x, y = validation(entry1.get(), entry2.get())
    # if x:
    #     text = f"{type(entry1.get())}, {type(entry2.get())}"
    # else:
    text = f"Dodano punkt: {entry1.get()}, {entry2.get()}."
    PUNKTY.append((x,y))
    altext = ""
    for point in PUNKTY:
        altext += str(point)
    toplabel.config(text=altext)
    label.config(text=text)

def button2_clicked():
    p = interpolation(float(entry3.get()))
    label.config(text=f"F({entry3.get()})={p}")
    
def button3_clicked():
    PUNKTY = ZADANIE
    altext = ""
    for point in PUNKTY:
        altext += str(point)
    toplabel.config(text=altext)
    p = interpolation(3.0)
    label.config(text=f"F(3)={p}")
    

# Tworzenie okna
root = tk.Tk()

# Tworzenie pól tekstowych
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# Tworzenie przycisków
button1 = tk.Button(root, text="Dodaj punkt", command=button1_clicked)
button2 = tk.Button(root, text="Policz wartosc", command=button2_clicked)
button3 = tk.Button(root, text="Zadanie z zajec", command=button3_clicked)

# Tworzenie pola tekstowego do wyświetlania tekstu
label = tk.Label(root, text="")
toplabel = tk.Label(root, text="")

# Umieszczanie elementów w oknie
toplabel.pack()
entry1.pack()
entry2.pack()
button1.pack()
entry3.pack()
button2.pack()
label.pack()
button3.pack()

# Uruchamianie pętli głównej programu
root.mainloop()
