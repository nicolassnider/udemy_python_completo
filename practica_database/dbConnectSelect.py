import json
import sqlite3

connect=sqlite3.connect("./DDBB/Ejemplo.db")

cursor=connect.cursor()

cursor.execute("SELECT * FROM personas")

#persona= cursor.fetchone()

personas=cursor.fetchall()

print(json.dumps(personas,indent=4))

for per in personas:
    print(f'''ID:\t{per[0]}\nNAME:\t{per[1]}\nAGE:\t{per[2]}\n''')