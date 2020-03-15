from tkinter import *

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
fileMenu.add_command(label="Salir", command=ventana.quit)


editMenu=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Editar", menu=editMenu)

helpMenu=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Ayuda", menu=helpMenu)

ventana.mainloop()