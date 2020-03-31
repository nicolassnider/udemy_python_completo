from tkinter import *
from tkinter import ttk

from practica_sistema_tkinter.conexion_db import AlumnosDB
from practica_sistema_tkinter.conexion_db.AlumnosDB import *
from practica_sistema_tkinter.conexion_db.consultas_db import *




class VistaAlumno(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def Nuevo():
            self.entryNombre.delete(0, END)
            self.entryEdad.delete(0, END)
            self.entryTelefono.delete(0, END)
            #self.entryCodCarrera.delete(0, END)
            self.comboBoxCarrera.delete(0,END)

            self.entryNombre.config(state='normal')
            self.entryEdad.config(state='normal')
            self.entryTelefono.config(state='normal')
            #self.entryCodCarrera.config(state='normal')
            self.comboBoxCarrera.config(state='normal')

            self.buttonGuardar.config(state='normal')

        # insert
        def insertarDatos():

            carrera=self.comboBoxCarrera.get()
            carrera = carrera[0]+carrera[1]

            query = "INSERT INTO alumno VALUES(NULL,?,?,?,?)"
            parametros = (
                #self.entryNombre.get(), self.entryEdad.get(), self.entryTelefono.get(), self.entryCodCarrera.get())
                self.entryNombre.get(), self.entryEdad.get(), self.entryTelefono.get(), carrera)

            conn = Conectar_bd()
            conn.Run_db(query, parametros)

            # actualizar tabla
            listarDatos()

            self.entryNombre.delete(0, END)
            self.entryEdad.delete(0, END)
            self.entryTelefono.delete(0, END)
            #self.entryCodCarrera.delete(0, END)

            self.entryNombre.config(state='readonly')
            self.entryEdad.config(state='readonly')
            self.entryTelefono.config(state='readonly')
            #self.entryCodCarrera.config(state='readonly')

        # delete
        def eliminarDatos():
            self.codigo_a = self.tabla.item(self.tabla.selection())['text']
            query = "DELETE FROM alumno WHERE codigo_a=?"
            parametros = (self.codigo_a)
            conn = Conectar_bd()
            conn.Run_db(query, (parametros,))
            listarDatos()

        # update
        def actualizarDatos(nombreN, edadN, telefonoN, codCarreraN,codigo):

            self.codigo_c = self.tabla.item(self.tabla.selection())['text']
            query="UPDATE alumno SET nombre_a=?,edad_a=?,telefono_a=?,codigo_c1=? WHERE codigo_a=?"
            parametros = (nombreN, edadN, telefonoN, codCarreraN,codigo)
            print(query, nombreN, edadN, telefonoN, codCarreraN, codigo)
            conn = Conectar_bd()
            conn.Run_db(query,parametros)
            self.ventana_editar.destroy()
            listarDatos()

        self.label_titulo = Label(self, text="Adm. Alumnos").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Campo nombre Alumno
        Label(self, text="Nombre de alumno").grid(row=1, column=0, padx=10, pady=10)
        self.entryNombre = Entry(self, state='readonly')
        self.entryNombre.grid(row=1, column=1)

        # Campo edad alumno
        Label(self, text="Edad").grid(row=2, column=0, padx=10, pady=10)
        self.entryEdad = Entry(self, state='readonly')
        self.entryEdad.grid(row=2, column=1)

        # Campo telefono alumno
        Label(self, text="Telefono").grid(row=3, column=0, padx=10, pady=10)
        self.entryTelefono = Entry(self, state='readonly')
        self.entryTelefono.grid(row=3, column=1)

        """# Campo carrera alumno
        Label(self, text="Carrera").grid(row=4, column=0, padx=10, pady=10)
        self.entryCodCarrera = Entry(self, state='readonly')
        self.entryCodCarrera.grid(row=4, column=1)"""
         # Como Box de Carreras
        self.label = Label(self, text="Escojer Carreras: ").grid(row=4, column=0, pady=10, padx=10)
        self.comboBoxCarrera = ttk.Combobox(self, state='readonly')
        self.comboBoxCarrera.grid(row=4, column=1, pady=10, padx=10)

        # Cargar Datos al combobox de Carreras
        def cargar_combo():
            query = 'SELECT codigo_c, nombre_c FROM carrera'
            conn = Conectar_bd()
            datos_c = conn.Run_db(query)

            for carrera in datos_c:
                values = list(self.comboBoxCarrera["values"])
                self.comboBoxCarrera["values"] = values + [(carrera[0], ',', carrera[1])]

        # Ejecutar Funcion
        cargar_combo()

        # Boton nuevo
        Button(self, text="Nuevo", command=Nuevo).grid(row=5, column=0, padx=10, pady=10)

        # Boton Guardar
        self.buttonGuardar= Button(self, text="Guardar", command=insertarDatos, state='disabled')
        self.buttonGuardar.grid(row=5, column=1, padx=10, pady=10)

        # Boton Eliminar
        Button(self, text="Eliminar", command=eliminarDatos).grid(row=7, column=0, padx=10, pady=10)

        # Tabla
        self.tabla = ttk.Treeview(self, column=('#0', '#1', '#2', '#3', '#4'))
        self.tabla.grid(row=6, column=0, columnspan=3)
        self.tabla.heading('#0', text="Código")
        self.tabla.heading('#1', text="Nombre")
        self.tabla.heading('#2', text="Edad")
        self.tabla.heading('#3', text="Telefono")
        self.tabla.heading('#4', text="Carrera")
        """self.tabla.heading('#5', text="Profesores")
        self.tabla.heading('#6', text="Materias")"""

        def editarDatos():

            codigo = self.tabla.item(self.tabla.selection())['text']

            nombreAntiguo = self.tabla.item(self.tabla.selection())['values'][0]

            edadAntiguo = self.tabla.item(self.tabla.selection())['values'][1]

            telefonoAntiguo = self.tabla.item(self.tabla.selection())['values'][2]

            codCarreraAntiguo = self.tabla.item(self.tabla.selection())['values'][3]

            # arranque ventana editar
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar Alumno")

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

            # label y campo de edad antiguo
            self.labelEdadAntiguo = Label(self.ventana_editar, text="Edad anterior")
            self.labelEdadAntiguo.grid(row=3, column=0, padx=10, pady=10)
            self.entryEdadAntiguo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=edadAntiguo), state='readonly')
            self.entryEdadAntiguo.grid(row=3, column=1, padx=10, pady=10)

            # label y campo de edad nuevo
            self.labelEdadNuevo = Label(self.ventana_editar, text="Edad Nuevo")
            self.labelEdadNuevo.grid(row=4, column=0, padx=10, pady=10)
            self.entryEdadNuevo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=edadAntiguo), state='normal')
            self.entryEdadNuevo.grid(row=4, column=1, padx=10, pady=10)

            # label y campo de teléfono antiguo
            self.labelTelefonoAntiguo = Label(self.ventana_editar, text="Teléfono anterior")
            self.labelTelefonoAntiguo.grid(row=5, column=0, padx=10, pady=10)
            self.entryTelefonoAntiguo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=telefonoAntiguo), state='readonly')
            self.entryTelefonoAntiguo.grid(row=5, column=1, padx=10, pady=10)

            # label y campo de teléfono nuevo
            self.labelTelefonoNuevo = Label(self.ventana_editar, text="Telefono nuevo")
            self.labelTelefonoNuevo.grid(row=6, column=0, padx=10, pady=10)
            self.entryTelefonoNuevo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=telefonoAntiguo), state='normal')
            self.entryTelefonoNuevo.grid(row=6, column=1, padx=10, pady=10)

            # label y campo de carrera antiguo
            self.labelCodCarreraAntiguo = Label(self.ventana_editar, text="Carrera anterior")
            self.labelCodCarreraAntiguo.grid(row=7, column=0, padx=10, pady=10)
            self.entryCodCarreraAntiguo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=codCarreraAntiguo), state='readonly')
            self.entryCodCarreraAntiguo.grid(row=7, column=1, padx=10, pady=10)

            # label y campo de edad nuevo
            self.labelCodCarreraNuevo = Label(self.ventana_editar, text="Carrera nuevo")
            self.labelCodCarreraNuevo.grid(row=8, column=0, padx=10, pady=10)
            self.entryCodCarreraNuevo = Entry(self.ventana_editar, textvariable=StringVar
            (self.ventana_editar, value=codCarreraAntiguo), state='normal')
            self.entryCodCarreraNuevo.grid(row=8, column=1, padx=10, pady=10)

            # boton actualizar
            self.botonActualizar = Button(self.ventana_editar, text="Actualizar Alumno",
                                          command=lambda: actualizarDatos
                                          (codigo=codigo, nombreN=self.entryNombreNuevo.get(), edadN=self.entryEdadNuevo.get(),
                                          telefonoN= self.entryTelefonoNuevo.get(), codCarreraN= self.entryCodCarreraNuevo.get()))

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
            """query = '''SELECT codigo_a,nombre_a,edad_a,telefono_a,nombre_c,nombre_p,nombre_m FROM alumno 
                    INNER JOIN carrera ON alumno.codigo_c1=carrera.codigo_c
                    INNER JOIN alumno_profe ap on alumno.codigo_a = ap.codigo_a1
                    INNER JOIN profesor p on ap.codigo_p1 = p.codigo_p
                    INNER JOIN materia_alumno ma on alumno.codigo_a = ma.codigo_a2
                    INNER JOIN materia ON ma.codigo_m1 = materia.codigo_m
                    ORDER BY codigo_a DESC'''"""
            query = '''SELECT codigo_a,nombre_a,edad_a,telefono_a,nombre_c FROM alumno 
                                INNER JOIN carrera ON alumno.codigo_c1=carrera.codigo_c'''
            conn = Conectar_bd
            datos = conn.Run_db(self, query=query)
            for alumno in datos:
                """self.tabla.insert('',0,text=alumno[0], values=(alumno[1],alumno[2],alumno[3],alumno[4],alumno[5],alumno[6]))"""
                self.tabla.insert('', 0, text=alumno[0], values=(alumno[1], alumno[2], alumno[3], alumno[4]))

        listarDatos()
