from tkinter import *
from tkinter import ttk

from practica_sistema_tkinter.conexion_db import AlumnosDB
from practica_sistema_tkinter.conexion_db.AlumnosDB import *
from practica_sistema_tkinter.conexion_db.consultas_db import *




class VistaProfesor(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def Nuevo():
            self.entryNombre.delete(0, END)
            self.entryTelefono.delete(0, END)
            self.entryDireccion.delete(0, END)

            self.entryNombre.config(state='normal')
            self.entryTelefono.config(state='normal')
            self.entryDireccion.config(state='normal')

        # insert
        def insertarDatos():
            query = "INSERT INTO profesor VALUES(NULL,?,?,?)"
            parametros = (
                self.entryNombre.get(), self.entryTelefono.get(), self.entryDireccion.get())

            conn = Conectar_bd()
            conn.Run_db(query, parametros)

            # actualizar tabla
            listarDatos()

            self.entryNombre.delete(0, END)
            self.entryTelefono.delete(0, END)
            self.entryDireccion.delete(0, END)

            self.entryNombre.config(state='readonly')
            self.entryTelefono.config(state='readonly')
            self.entryDireccion.config(state='readonly')

        # delete
        def eliminarDatos():
            self.codigo_p = self.tabla.item(self.tabla.selection())['text']
            query = "DELETE FROM profesor WHERE codigo_p=?"
            parametros = (self.codigo_p)
            conn = Conectar_bd()
            conn.Run_db(query, (parametros,))
            listarDatos()

        # update
        def actualizarDatos(nombreN, telefonoN, direccionN, codigo):

            self.codigo_c = self.tabla.item(self.tabla.selection())['text']
            query="UPDATE profesor SET nombre_p=?,telefono_p=?,direccion_p=? WHERE codigo_p=?"
            parametros = (nombreN, telefonoN, direccionN, codigo)
            conn = Conectar_bd()
            conn.Run_db(query,parametros)
            self.ventana_editar.destroy()
            listarDatos()

        self.label_titulo = Label(self, text="Adm. Profesores").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo nombre Profesor
        Label(self, text="Nombre de Profesor").grid(row=1, column=0, padx=10, pady=10)
        self.entryNombre = Entry(self, state='readonly')
        self.entryNombre.grid(row=1, column=1)

        # Campo telefono Profesor
        Label(self, text="Telefono").grid(row=2, column=0, padx=10, pady=10)
        self.entryTelefono = Entry(self, state='readonly')
        self.entryTelefono.grid(row=2, column=1)

        # Campo direccion Profesor
        Label(self, text="Dirección").grid(row=3, column=0, padx=10, pady=10)
        self.entryDireccion = Entry(self, state='readonly')
        self.entryDireccion.grid(row=3, column=1)

        # Boton nuevo
        Button(self, text="Nuevo", command=Nuevo).grid(row=4, column=0, padx=10, pady=10)

        # Boton Guardar
        Button(self, text="Guardar", command=insertarDatos).grid(row=4, column=1, padx=10, pady=10)

        # Boton Eliminar
        Button(self, text="Eliminar", command=eliminarDatos).grid(row=7, column=0, padx=10, pady=10)

        # Tabla
        self.tabla = ttk.Treeview(self, column=('#0', '#1', '#2'))
        self.tabla.grid(row=6, column=0, columnspan=3)
        self.tabla.heading('#0', text="Código")
        self.tabla.heading('#1', text="Nombre")
        self.tabla.heading('#2', text="Telefono")
        self.tabla.heading('#3', text="Dirección")

        def editarDatos():

            codigo = self.tabla.item(self.tabla.selection())['text']

            nombreAntiguo = self.tabla.item(self.tabla.selection())['values'][0]

            telefonoAntiguo = self.tabla.item(self.tabla.selection())['values'][1]

            direccionAntiguo = self.tabla.item(self.tabla.selection())['values'][2]

            # arranque ventana editar
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Profesor")

            # label y campo nombre
            self.labelCodigo = Label(self.ventana_editar, text="Código: ")
            self.labelCodigo.grid(row=0, column=0, padx=10, pady=10)
            self.entryCodigo = Entry(self.ventana_editar, textvariable=
            StringVar(self.ventana_editar, value=codigo), state='readonly')
            self.entryCodigo.grid(row=0, column=1, padx=10, pady=10)

            # label y campo de nombre antiguo
            self.labelNombreAntiguo = Label(self.ventana_editar, text="Nombre anterior")
            self.labelNombreAntiguo.grid(row=1, column=0, padx=10, pady=10)
            self.entryNombreAntiguo = Entry(self.ventana_editar, textvariable=
            StringVar(self.ventana_editar, value=nombreAntiguo), state='readonly')
            self.entryNombreAntiguo.grid(row=1, column=1, padx=10, pady=10)

            # label y campo de nombre nuevo
            self.labelNombreNuevo = Label(self.ventana_editar, text="Nombre Nuevo")
            self.labelNombreNuevo.grid(row=2, column=0, padx=10, pady=10)
            self.entryNombreNuevo = Entry(self.ventana_editar, textvariable=
            StringVar(self.ventana_editar, value=nombreAntiguo), state='normal')
            self.entryNombreNuevo.grid(row=2, column=1, padx=10, pady=10)

            # label y campo de telefono antiguo
            self.labelTelefonoAntiguo = Label(self.ventana_editar, text="Telefono anterior")
            self.labelTelefonoAntiguo.grid(row=3, column=0, padx=10, pady=10)
            self.entryTelefonoAntiguo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=telefonoAntiguo), state='readonly')
            self.entryTelefonoAntiguo.grid(row=3, column=1, padx=10, pady=10)

            # label y campo de teléfono nuevo
            self.labelTelefonoNuevo = Label(self.ventana_editar, text="Teléfono Nuevo")
            self.labelTelefonoNuevo.grid(row=4, column=0, padx=10, pady=10)
            self.entryTelefonoNuevo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=telefonoAntiguo), state='normal')
            self.entryTelefonoNuevo.grid(row=4, column=1, padx=10, pady=10)

            # label y campo de dirección antiguo
            self.labelTelefonoAntiguo = Label(self.ventana_editar, text="Dirección anterior")
            self.labelTelefonoAntiguo.grid(row=7, column=0, padx=10, pady=10)
            self.entryTelefonoAntiguo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=direccionAntiguo), state='readonly')
            self.entryTelefonoAntiguo.grid(row=7, column=1, padx=10, pady=10)

            # label y campo de dirección nuevo
            self.labelDireccionNuevo = Label(self.ventana_editar, text="Dirección nuevo")
            self.labelDireccionNuevo.grid(row=8, column=0, padx=10, pady=10)
            self.entryDireccionNuevo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=direccionAntiguo), state='normal')
            self.entryDireccionNuevo.grid(row=8, column=1, padx=10, pady=10)

            # boton actualizar
            self.botonActualizar = Button(self.ventana_editar, text="Actualizar Profesor",
                                          command=lambda: actualizarDatos
                                          (codigo=codigo, nombreN=self.entryNombreNuevo.get(),
                                           telefonoN= self.entryTelefonoNuevo.get(), direccionN= self.entryDireccionNuevo.get()))

            self.botonActualizar.grid(row=9, column=0, columnspan=2, pady=10, padx=10)

        # Boton Editar
        Button(self, text="Editar", command=editarDatos).grid(row=7, column=1, padx=10, pady=10)

        # listar Datos
        def listarDatos():
            # eliminar datos de la tabla
            recorrerTabla = self.tabla.get_children()
            for elementos in recorrerTabla:
                self.tabla.delete(elementos)

            # ejecuta la consulta y carga datos a la tabla
            query = "SELECT * FROM profesor ORDER BY codigo_p DESC"
            conn = Conectar_bd
            datos = conn.Run_db(self, query=query)
            for profesor in datos:
                self.tabla.insert('',0,text=profesor[0], values=(profesor[1],profesor[2],profesor[3]))

        listarDatos()
