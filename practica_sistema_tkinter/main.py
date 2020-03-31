from tkinter import *

from vistas.navegador import *

if __name__ == '__main__':
    ventana = Tk()
    ventana.config(padx=10,pady=10)
    #ventana.geometry("1024x768")
    ventana.resizable(False,False)
    app = Aplicacion(ventana)

    ventana.mainloop()
