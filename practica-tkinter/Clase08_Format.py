from tkinter import *

ventana=Tk()
ventana.config(bg="#3CB371")

miFrame=Frame(ventana,width=200, height=200)
miFrame.pack()

#Labels
labelUser= Label(miFrame,text="Usuario: ")
labelUser.grid(row=0,column=0,pady=10,padx=10)

labelPass= Label(miFrame,text="Password: ")
labelPass.grid(row=1,column=0,pady=10,padx=10)

#Entries
textoUser= Entry(miFrame,justify="center")
textoUser.grid(row=0,column=1,pady=10,padx=10)

textoPassword= Entry(miFrame,justify="center",show="*")
textoPassword.grid(row=1,column=1,pady=10,padx=10)

#Button
botonAceptar=Button(miFrame,text="Aceptar",command=exit)
botonAceptar.grid(row=2,column=0,pady=10,padx=10,columnspan=2)
botonAceptar.config(width=30)

ventana.mainloop()