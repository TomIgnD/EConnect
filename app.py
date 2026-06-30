"""
=========================================
            ECONNECT
       Administrador escolar
=========================================
"""

import os
import sqlite3

# Crear la base de datos

RUTA_BD = "database/econnect.db"
RUTA_SQL = "database/econnect.sql"

os.makedirs("database", exist_ok=True)

conexion = sqlite3.connect(RUTA_BD)
cursor = conexion.cursor()

# Activar claves foráneas
cursor.execute("PRAGMA foreign_keys = ON;")

# Crear las tablas

if os.path.exists(RUTA_SQL):

    with open(RUTA_SQL, "r", encoding="utf-8") as archivo:

        script = archivo.read()

    cursor.executescript(script)

    conexion.commit()

    print("Base de datos lista.")

else:

    print("No se encontró el archivo econnect.sql")

cursor.close()
conexion.close()

# Iniciar Flask

from modules.web import app

print("===========================")
print("        ECONNECT")
print("===========================")
print("Servidor iniciado.")
print()

app.run(debug=True)