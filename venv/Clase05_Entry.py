from tkinter import *

def imprimir():
    label01=Label(miFrame,text=texto1.get())
    label01.pack()
    label01.config(bg="black",fg="green")
    label01.config()

ventana=Tk()
ventana.geometry("630x360")

miFrame=Frame(ventana,width=630,height=360)
miFrame.place(x=1,y=1)

texto1= Entry(miFrame)
texto1.pack()
texto1.config(fon=("arial black",16))
texto1.config(bg="red",fg="blue")

boton01=Button(miFrame,text="Imprimir",command=imprimir)
boton01.pack()



ventana.mainloop()