import sqlite3

class Conectar_bd():
    global nombre_db
    nombre_db=".\sistema_universitario.db"

    def Run_db (self, query, parametros=()):

        with sqlite3.connect(nombre_db) as conn:
            cursor = conn.cursor()

            datos=cursor.execute(query,parametros)

            conn.commit()

        return datos


