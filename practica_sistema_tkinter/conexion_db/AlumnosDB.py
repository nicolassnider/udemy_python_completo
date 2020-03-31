import sqlite3

class AlumnosDB():
    global nombre_db
    nombre_db=".\sistema_universitario.db"


    def updateAlumno (self, query, nombreN, edadN, telefonoN, codCarreraN,codigo):
        print(query, nombreN, edadN, telefonoN, codCarreraN,codigo)
        with sqlite3.connect(nombre_db) as conn:
            cursor = conn.cursor()

            datos=cursor.execute(query,(nombreN, edadN, telefonoN, codCarreraN,codigo))

            conn.commit()

        return datos