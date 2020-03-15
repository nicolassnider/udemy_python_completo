from tkinter import *

def seleccionar():
    cadena=""

    if(marcar01.get()):
        cadena+="Marcar 01 "
    else:
        cadena+="Desmarcar 01 "
    if(marcar02.get()):
        cadena+="Marcar 02 "
    else:
        cadena+="Desmarcar 02 "

    mostrar.config(text=cadena)

ventana = Tk()

marcar01= IntVar()
marcar02= IntVar()

Checkbutton(ventana, text = "Marcar 01", variable= marcar01,onvalue=1,offvalue=0,command=seleccionar).pack()
Checkbutton(ventana, text = "Marcar 02", variable= marcar02, onvalue=1,offvalue=0,command=seleccionar).pack()

mostrar = Label(ventana)
mostrar.pack()

ventana.mainloop()