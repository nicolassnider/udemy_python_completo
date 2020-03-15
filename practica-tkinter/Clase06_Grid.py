from tkinter import *

def Saludar():
    pass

ventana = Tk()

ventana.config(bg="#3CB371")

espacio01 = Frame(ventana, width = 200, height= 200, bg= "#2E8B57")
espacio01.pack()
#Labels
labelNombre=Label(espacio01, text= "Nombre: ")
labelNombre.grid(row=0, column=0, pady=10, padx=10)

labelApe = Label(espacio01, text="Ape: ")
labelApe.grid(row=1, column=0, pady=10, padx=10)

labelTel = Label(espacio01, text="Tel: ")
labelTel.grid(row=2, column=0, pady=10, padx=10)

#Entrys
textoNombre = Entry(espacio01, text="Nombre: ")
textoNombre.grid(row=0, column=1, pady=10, padx=10)

textoApe = Entry(espacio01, text="Ape: ")
textoApe.grid(row=1, column=1, pady=10, padx=10)

textoTel = Entry(espacio01, text="Tel: ")
textoTel.grid(row=2, column=1, pady=10, padx=10)

#Buttons
butNombre=Button(espacio01, text="Saludar", command=Saludar)
butNombre.grid(row=0, column=2, pady=10, padx=10)

butNombre=Button(espacio01, text="Saludar", command=Saludar)
butNombre.grid(row=1, column=2, pady=10, padx=10)

butNombre=Button(espacio01, text="Saludar", command=Saludar)
butNombre.grid(row=2, column=2, pady=10, padx=10)

ventana.mainloop()