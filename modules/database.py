import sqlite3

conexion = sqlite3.connect("database/econnect.db", check_same_thread=False)

# Activar claves foráneas
conexion.execute("PRAGMA foreign_keys = ON")

cursor = conexion.cursor()



def insertar_cooperadora_bd(precio, pagos):

    cursor.execute(
        "INSERT INTO Cooperadora (Precio_mate_x_anio, Pagos_pendientes) VALUES (?, ?)",
        (precio, pagos)
    )

    conexion.commit()



def insertar_area_bd(id_coop, materias, promedio):

    cursor.execute(
        "INSERT INTO Areas (ID_cooperadora, Materias, Promedio) VALUES (?, ?, ?)",
        (id_coop, materias, promedio)
    )

    conexion.commit()



def insertar_especialidad_bd(id_area, cant_alum, turno):

    cursor.execute(
        "INSERT INTO Especialidades (ID_Areas, Cant_alum, Turno) VALUES (?, ?, ?)",
        (id_area, cant_alum, turno)
    )

    conexion.commit()



def insertar_tiene_bd(id_area, id_especialidad):

    cursor.execute(
        "INSERT INTO Tiene (ID_Areas, ID_especialidades) VALUES (?, ?)",
        (id_area, id_especialidad)
    )

    conexion.commit()



def insertar_profesor_bd(dni, puntaje, cursos, nombre):

    cursor.execute(
        """
        INSERT INTO Profesor
        (DNI_profesor, Puntuaje, Cursos, Nombre)
        VALUES (?, ?, ?, ?)
        """,
        (dni, puntaje, cursos, nombre)
    )

    conexion.commit()



def insertar_materia_bd(dni_prof, id_especialidad, temas, anio):

    cursor.execute(
        """
        INSERT INTO Materia
        (DNI_profesor, ID_especialidades, Temas, Anio)
        VALUES (?, ?, ?, ?)
        """,
        (dni_prof, id_especialidad, temas, anio)
    )

    conexion.commit()



def insertar_divide_bd(id_materia, id_especialidad):

    cursor.execute(
        "INSERT INTO Divide (ID_materia, ID_especialidades) VALUES (?, ?)",
        (id_materia, id_especialidad)
    )

    conexion.commit()



def insertar_alumno_bd(dni, nro_alumno, nombre, mate_adeudadas):

    cursor.execute(
        """
        INSERT INTO Alumnos
        (DNI_alumno, Nro_alumno, Nombre, Mate_adeudadas)
        VALUES (?, ?, ?, ?)
        """,
        (dni, nro_alumno, nombre, mate_adeudadas)
    )

    conexion.commit()



def insertar_curso_bd(id_materia, dni_alumno, promedio, turno, horarios):

    cursor.execute(
        """
        INSERT INTO Curso
        (ID_materia, DNI_alumno, Promedio, Turno, Horarios)
        VALUES (?, ?, ?, ?, ?)
        """,
        (id_materia, dni_alumno, promedio, turno, horarios)
    )

    conexion.commit()



def insertar_hay_bd(id_materia, nro_curso):

    cursor.execute(
        "INSERT INTO Hay (ID_materia, Nro_curso) VALUES (?, ?)",
        (id_materia, nro_curso)
    )

    conexion.commit()



def insertar_quedan_bd(dni_alumno, nro_curso):

    cursor.execute(
        "INSERT INTO Quedan (DNI_alumno, Nro_curso) VALUES (?, ?)",
        (dni_alumno, nro_curso)
    )

    conexion.commit()