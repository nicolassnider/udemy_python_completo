from tkinter import *

ventana=Tk()
ventana.config(bg="black")

miFrame=Frame(ventana)
miFrame.pack()

campoTexto=Text(miFrame)
campoTexto.grid(row=0,column=0)
campoTexto.config(width=20,height=10)
campoTexto.config(bg="black",fg="green",fon=("arial",20))

scrollVertical=Scrollbar(miFrame, command=campoTexto.yview)
scrollVertical.grid(row=0,column=1,sticky="nesw")
campoTexto.config(yscrollcommand=scrollVertical.set)

ventana.mainloop()