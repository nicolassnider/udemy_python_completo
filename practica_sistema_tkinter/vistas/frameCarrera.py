from tkinter import *
from tkinter import ttk

from practica_sistema_tkinter.conexion_db.consultas_db import Conectar_bd


class VistaCarrera(ttk.Frame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        def Nuevo():
            self.entryNombre.delete(0,END)
            self.entryDuracion.delete(0, END)
            self.entryNombre.config(state='normal')
            self.entryDuracion.config(state='normal')
        # insert
        def insertarDatos():
            query="INSERT INTO carrera VALUES(NULL,?,?)"
            parametros=(self.entryNombre.get(),self.entryDuracion.get())

            conn= Conectar_bd()
            conn.Run_db(query,parametros)

            #actualizar tabla
            listarDatos()

            self.entryNombre.delete(0, END)
            self.entryDuracion.delete(0, END)
            self.entryNombre.config(state='readonly')
            self.entryDuracion.config(state='readonly')

        # delete
        def eliminarDatos():
            self.codigo_c = self.tabla.item(self.tabla.selection())['text']
            query="DELETE FROM carrera WHERE codigo_c=?"
            parametros = (self.codigo_c)
            conn= Conectar_bd()
            conn.Run_db(query,(parametros,))
            listarDatos()

        # update
        def actualizarDatos(codigoN,codigoA,nombreN,nombreA,duracionN,duracionA):

            self.codigo_c = self.tabla.item(self.tabla.selection())['text']
            query="UPDATE carrera SET codigo_c=?,nombre_c=?,duracion_c=? WHERE codigo_c=? and nombre_c=? and duracion_c=?"
            parametros = (codigoN,nombreN,duracionN,codigoA,nombreA,duracionA)
            conn= Conectar_bd()
            conn.Run_db(query,(parametros))
            self.ventana_editar.destroy()
            listarDatos()


        self.label_titulo= Label(self,text="Adm. Carreras").grid(row=0,column=0, columnspan=2,padx=10,pady=10)

        #Campo nombre carrera
        Label(self, text="Nombre de carrera").grid(row=1, column=0,padx=10,pady=10)
        self.entryNombre=Entry(self, state='readonly')
        self.entryNombre.grid(row=1,column=1)

        # Campo duracion carrera
        Label(self, text="Duración").grid(row=2, column=0,padx=10,pady=10)
        self.entryDuracion = Entry(self, state='readonly')
        self.entryDuracion.grid(row=2, column=1)

        #Boton nuevo
        Button(self, text="Nuevo", command=Nuevo).grid(row=3, column=0,padx=10,pady=10)

        # Boton Guardar
        Button(self, text="Guardar",command=insertarDatos).grid(row=3, column=1,padx=10,pady=10)

        # Boton Eliminar
        Button(self, text="Eliminar", command=eliminarDatos).grid(row=6, column=0, padx=10, pady=10)



        # Tabla
        self.tabla= ttk.Treeview(self, column=('',''))
        self.tabla.grid(row=5, column=0,columnspan=3)
        self.tabla.heading('#0', text="Código")
        self.tabla.heading('#1', text="Nombre")
        self.tabla.heading('#2', text="Duración")



        def editarDatos():

            codigo = self.tabla.item(self.tabla.selection())['text']

            nombreAntiguo = self.tabla.item(self.tabla.selection())['values'][0]

            duracionAntiguo = self.tabla.item(self.tabla.selection())['values'][1]

            print(codigo)
            print(nombreAntiguo)
            print(duracionAntiguo)

            #arranque ventana editar
            self.ventana_editar= Toplevel()
            self.ventana_editar.title("Editar Carrera")

            #label y campo nombre
            self.labelCodigo = Label(self.ventana_editar,text="Código: ")
            self.labelCodigo.grid(row=0,column=0,padx=10,pady=10)
            self.entryCodigo=Entry(self.ventana_editar,textvariable = StringVar(self.ventana_editar,value=codigo), state='readonly')
            self.entryCodigo.grid(row=0,column=1,padx=10,pady=10)

            #label y campo de nombre antiguo
            self.labelNombreAntiguo = Label(self.ventana_editar,text="Nombre anterior")
            self.labelNombreAntiguo.grid(row=1,column=0,padx=10,pady=10)
            self.entryNombreAntiguo=Entry(self.ventana_editar,textvariable = StringVar(self.ventana_editar,value=nombreAntiguo), state='readonly')
            self.entryNombreAntiguo.grid(row=1,column=1,padx=10,pady=10)

            # label y campo de nombre nuevo
            self.labelNombreNuevo = Label(self.ventana_editar, text="Nombre nuevo")
            self.labelNombreNuevo.grid(row=2, column=0, padx=10, pady=10)
            self.entryNombreNuevo = Entry(self.ventana_editar)
            self.entryNombreNuevo.grid(row=2, column=1, padx=10, pady=10)

            # label y campo de duración antiguo
            self.labelDuracionAntiguo = Label(self.ventana_editar, text="Duración anterior")
            self.labelDuracionAntiguo.grid(row=3, column=0, padx=10, pady=10)
            self.entryDuracionAntiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value=duracionAntiguo), state='readonly')
            self.entryDuracionAntiguo.grid(row=3, column=1, padx=10, pady=10)

            # label y campo de duración nuevo
            self.labelDuracionNuevo = Label(self.ventana_editar, text="duración nuevo")
            self.labelDuracionNuevo.grid(row=4, column=0, padx=10, pady=10)
            self.entryDuracionNuevo = Entry(self.ventana_editar)
            self.entryDuracionNuevo.grid(row=4, column=1, padx=10, pady=10)

            # boton actualizar
            self.botonActualizar=Button(self.ventana_editar,text="Actualizar Carrera", command= lambda :actualizarDatos(codigo,codigo, self.entryNombreNuevo.get(),nombreAntiguo,self.entryDuracionNuevo.get(),duracionAntiguo))

            self.botonActualizar.grid(row=5, column=0,columnspan=2,pady=10,padx=10)

        # Boton Editar
        Button(self, text="Editar", command=editarDatos).grid(row=6, column=1 , padx=10, pady=10)

        #listar Datos
        def listarDatos():
            #eliminar datos de la tabla
            recorrerTabla=self.tabla.get_children()
            for elementos in recorrerTabla:
                self.tabla.delete(elementos)

            #ejecuta la consulta y carga datos a la tabla
            query = "SELECT * FROM carrera ORDER BY codigo_c DESC"
            conn = Conectar_bd
            datos=conn.Run_db(self,query=query)
            for carrera in datos:
                self.tabla.insert('',0,text=carrera[0], values=(carrera[1],carrera[2]))




        listarDatos()







