from tkinter import *
from tkinter import messagebox

#---ventanas simples
def informacion():
    messagebox.showinfo("Hola","Cortado")

def advertencia():
    messagebox.showwarning("Hola","Cortado")

def error():
    messagebox.showerror("Hola","Cortado")
#---ventanas avanzadas
def pregunta():
    #valor=messagebox.askquestion("Salir","Seguro?")#yes or no
    valor=messagebox.askyesno("Salir","Seguro?")#true or false
    if valor:
        ventana.quit()


ventana=Tk()

menuBar= Menu(ventana)
ventana.config(menu=menuBar)

fileMenu=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Archivo", menu=fileMenu)
fileMenu.add_command(label="Nuevo")
fileMenu.add_separator()
fileMenu.add_command(label="Abrir")
fileMenu.add_separator()
fileMenu.add_command(label="Guardar")
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=pregunta)


editMenu=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Editar", menu=editMenu)
editMenu.add_command(label="Copiar")
editMenu.add_separator()
editMenu.add_command(label="Cortar",command=informacion)
editMenu.add_separator()
editMenu.add_command(label="Pegar")


helpMenu=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Ayuda", menu=helpMenu)

ventana.mainloop()