from tkinter import *

def Saludar():

    labelSaludar = Label(miFrame, text="Hola alumno")
    labelSaludar.place(x=200, y=10)

ventana= Tk()
ventana.geometry("630x630")

miFrame=Frame(ventana, width = "630", height="630")
miFrame.place(x=1,y=1)

boton01=Button(miFrame, text="Saludar", command=Saludar)
boton01.place(x=1,y=1)
boton01.config(bg="red", fg="blue")
boton01.config(fon=("consolas",16))

imagen=PhotoImage(file="./sources/airbnb-brands.png")

button02=Button(miFrame,image=imagen,command=Saludar)
button02.place(x=50,y=100)

ventana.mainloop()
