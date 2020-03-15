from tkinter import *

ventana = Tk()
ventana.title("hola Mundo!")
ventana.iconbitmap("./sources/icon.ico")
ventana.geometry("630x360")
ventana.config(bg="blue")
ventana.resizable(FALSE, FALSE)

miFrame = Frame(ventana, width="300", height="250", bg="green")
miFrame.place(x=1,y=1)
#miFrame.place(x=20, y=100)
miFrame.pack(side="left", anchor="s")
miFrame.config(width="200", height="200")
miFrame.config(bg="green", bd=25)
miFrame.config(relief="groove", cursor="pirate")

ventana.mainloop()
