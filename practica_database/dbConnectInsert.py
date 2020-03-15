import sqlite3
conexion = sqlite3.connect("./DDBB/Ejemplo.db")
cursor= conexion.cursor()

personas=[("Pedro",15),("Roberto",35),("Maria",65)]



try:
    '''cursor.execute("""CREATE TABLE "personas" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nombre"	VARCHAR(80) NOT NULL,
	"edad"	INTEGER NOT NULL
);""")'''
    #cursor.execute("""INSERT INTO "personas"("nombre","edad") VALUES ('Juan',34);""")    
    cursor.executemany("""INSERT INTO "personas"("nombre","edad") VALUES (?,?);""",personas)
    conexion.commit()
    print("query ok")
except Exception:
    print("query NO ok")
finally:
    conexion.close()
