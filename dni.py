from tkinter import *
a = "Daniel Mauricio Chumacero Lozano"
b = "Vicente Paul Valdera Muñoz"
c = "Julio Cesar Velasquez Racchumi"

def calcular():
    if num.get() == 79299994:
        dni = a
    elif num.get ()== 46924587:
        dni = b
    elif num.get ()== 73875390:
        dni = c
    else:
        dni = "No encontrados"
    res.set("Nombres y Apellidos: " + dni)

ventana = Tk()

num = IntVar()
res = StringVar()
ventana.geometry ("400x300")

textoN = Label(ventana,text="Ingrese DNI: ")
textoN.place(x=150,y=10)

caja = Entry(ventana,textvariable=num)
caja.place(x=150,y=50)

textoR = Label(ventana,textvariable=res)
textoR.place(x=50,y=140)

boton = Button(ventana,text="Buscar",command=calcular, )
boton.place (x=180, y=100)
ventana.mainloop()
