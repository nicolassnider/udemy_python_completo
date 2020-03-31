from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

from practica_sistema_tkinter.vistas.frameAlumno import VistaAlumno
from practica_sistema_tkinter.vistas.frameCarrera import VistaCarrera
from practica_sistema_tkinter.vistas.frameMateria import VistaMateria
from practica_sistema_tkinter.vistas.frameProfesor import VistaProfesor


class Aplicacion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ventana = ventana
        self.ventana.iconbitmap("./img/uni.ico")

        self.ventana.title("Sistema Universitario")

        # Paneles
        self.navegador = Notebook(self)

        # Panel inicio
        self.inicio = Label(self.navegador, text="Pagina de inicio")
        self.navegador.add(self.inicio, text="Inicio")
        # Panel carrera
        self.abm_carreras = VistaCarrera()
        self.navegador.add(self.abm_carreras, text="Carreras")
        # Panel carrera
        self.abm_profesores = VistaProfesor(self.navegador)
        self.navegador.add(self.abm_profesores, text="Profesores")
        # Panel alumno
        self.abm_alumnos = VistaAlumno()
        self.navegador.add(self.abm_alumnos, text="Alumnos")
        # Panel materia
        self.abm_materias = VistaMateria(self.navegador)
        self.navegador.add(self.abm_materias, text="Materias")

        self.navegador.pack()
        self.pack()
