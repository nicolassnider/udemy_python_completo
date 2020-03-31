from tkinter import *
from tkinter import ttk

from practica_sistema_tkinter.conexion_db import AlumnosDB
from practica_sistema_tkinter.conexion_db.AlumnosDB import *
from practica_sistema_tkinter.conexion_db.consultas_db import *




class VistaMateria(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def Nuevo():
            self.entryNombre.delete(0, END)
            self.entryCreditos.delete(0, END)

            self.entryNombre.config(state='normal')
            self.entryCreditos.config(state='normal')

        # insert
        def insertarDatos():
            query = "INSERT INTO materia VALUES(NULL,?,?)"
            parametros = (
                self.entryNombre.get(), self.entryCreditos.get())

            conn = Conectar_bd()
            conn.Run_db(query, parametros)

            # actualizar tabla
            listarDatos()

            self.entryCreditos.delete(0, END)
            self.entryCreditos.delete(0, END)
            self.entryCreditos.delete(0, END)

            self.entryCreditos.config(state='readonly')
            self.entryCreditos.config(state='readonly')
            self.entryCreditos.config(state='readonly')

        # delete
        def eliminarDatos():
            self.codigo_m = self.tabla.item(self.tabla.selection())['text']
            query = "DELETE FROM materia WHERE codigo_m=?"
            parametros = (self.codigo_m)
            conn = Conectar_bd()
            conn.Run_db(query, (parametros,))
            listarDatos()

        # update
        def actualizarDatos(nombreN, creditosN, codigo):

            self.codigo_c = self.tabla.item(self.tabla.selection())['text']
            query="UPDATE materia SET nombre_m=?,creditos_m=? WHERE codigo_m=?"
            parametros = (nombreN, creditosN, codigo)
            conn = Conectar_bd()
            conn.Run_db(query,parametros)
            self.ventana_editar.destroy()
            listarDatos()

        self.label_titulo = Label(self, text="Adm. Materias").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo nombre Materia
        Label(self, text="Nombre de Materia").grid(row=1, column=0, padx=10, pady=10)
        self.entryNombre = Entry(self, state='readonly')
        self.entryNombre.grid(row=1, column=1)

        # Campo creditos Materia
        Label(self, text="Creditos").grid(row=2, column=0, padx=10, pady=10)
        self.entryCreditos = Entry(self, state='readonly')
        self.entryCreditos.grid(row=2, column=1)

        # Boton nuevo
        Button(self, text="Nuevo", command=Nuevo).grid(row=3, column=0, padx=10, pady=10)

        # Boton Guardar
        Button(self, text="Guardar", command=insertarDatos).grid(row=3, column=1, padx=10, pady=10)

        # Boton Eliminar
        Button(self, text="Eliminar", command=eliminarDatos).grid(row=7, column=0, padx=10, pady=10)

        # Tabla
        self.tabla = ttk.Treeview(self, column=('#0', '#1'))
        self.tabla.grid(row=6, column=0, columnspan=3)
        self.tabla.heading('#0', text="Código")
        self.tabla.heading('#1', text="Nombre")
        self.tabla.heading('#2', text="Creditos")

        def editarDatos():

            codigo = self.tabla.item(self.tabla.selection())['text']

            nombreAntiguo = self.tabla.item(self.tabla.selection())['values'][0]

            creditosAntiguo = self.tabla.item(self.tabla.selection())['values'][1]

            # arranque ventana editar
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Materia")

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
            self.labelCreditosAntiguo = Label(self.ventana_editar, text="Telefono anterior")
            self.labelCreditosAntiguo.grid(row=3, column=0, padx=10, pady=10)
            self.entryCreditosAntiguo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=creditosAntiguo), state='readonly')
            self.entryCreditosAntiguo.grid(row=3, column=1, padx=10, pady=10)

            # label y campo de teléfono nuevo
            self.labelCreditosNuevo = Label(self.ventana_editar, text="Teléfono Nuevo")
            self.labelCreditosNuevo.grid(row=4, column=0, padx=10, pady=10)
            self.entryCreditosNuevo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=creditosAntiguo), state='normal')
            self.entryCreditosNuevo.grid(row=4, column=1, padx=10, pady=10)

            # boton actualizar
            self.botonActualizar = Button(self.ventana_editar, text="Actualizar Materia",
                                          command=lambda: actualizarDatos
                                          (codigo=codigo, nombreN=self.entryNombreNuevo.get(),
                                           creditosN= self.entryCreditosNuevo.get()))

            self.botonActualizar.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        # Boton Editar
        Button(self, text="Editar", command=editarDatos).grid(row=7, column=1, padx=10, pady=10)

        # listar Datos
        def listarDatos():
            # eliminar datos de la tabla
            recorrerTabla = self.tabla.get_children()
            for elementos in recorrerTabla:
                self.tabla.delete(elementos)

            # ejecuta la consulta y carga datos a la tabla
            query = "SELECT * FROM materia ORDER BY codigo_m DESC"
            conn = Conectar_bd
            datos = conn.Run_db(self, query=query)
            for materia in datos:
                self.tabla.insert('',0,text=materia[0], values=(materia[1],materia[2]))

        listarDatos()
