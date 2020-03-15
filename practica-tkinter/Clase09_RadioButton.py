from tkinter import * 

ventana=Tk()

def seleccionado():
    label1.config(text=opcion.get())
def reiniciar():
    opcion.set(None)
    label1.config(text="")

opcion = IntVar()

Radiobutton(ventana, text="opcion1",variable = opcion,value=1,command=seleccionado).pack()
Radiobutton(ventana, text="opcion2",variable = opcion,value=2,command=seleccionado).pack()
Radiobutton(ventana, text="opcion3",variable = opcion,value=3,command=seleccionado).pack()

label1=Label(ventana)
label1.pack()

Button(ventana,text = "Limpiar", command= reiniciar).pack()

ventana.mainloop()