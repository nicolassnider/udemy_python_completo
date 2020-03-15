from tkinter import *

ventana = Tk()
ventana.title("hola Mundo, Label!")
ventana.iconbitmap("./sources/icon.ico")
ventana.geometry("630x360")

miFrame = Frame(ventana, width="400", height="300", bg="green")
miFrame.place(x=1, y=1)

label01 = Label(miFrame, text="Hola Mundo!")
label01.place(x=10, y=10)
label01.config(bg="red", fg="blue")
label01.config(fon=("arial", 20))

print(label01.cget('text'))
print(label01.cget('fon'))

image = PhotoImage(file="./sources/random.png")
image.zoom(x=50,y=50)
label02 = Label(miFrame, image = image).place(x=50, y=50)
ventana.mainloop()