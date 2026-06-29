import mysql.connector

conexion = mysql.connector.connect(
    host="YOUR_HOST",
    user="YOUR_USER",
    password="YOUR_PASSWORD",
    database="YOUR_DATABASE"
)

cursor = conexion.cursor()


def insertar_cooperadora_bd(precio, pagos):
    cursor.execute(
        "INSERT INTO Cooperadora (Precio_mate_x_año, Pagos_pendientes) VALUES (%s,%s)",
        (precio, pagos)
    )
    conexion.commit()


def insertar_area_bd(id_coop, materias, promedio):
    cursor.execute(
        "INSERT INTO Areas (ID_cooperadora, Materias, Promedio) VALUES (%s,%s,%s)",
        (id_coop, materias, promedio)
    )
    conexion.commit()


def insertar_especialidad_bd(id_area, cant_alum, turno):
    cursor.execute(
        "INSERT INTO Especialidades (ID_Areas, Cant_alum, Turno) VALUES (%s,%s,%s)",
        (id_area, cant_alum, turno)
    )
    conexion.commit()


def insertar_tiene_bd(id_area, id_especialidad):
    cursor.execute(
        "INSERT INTO Tiene (ID_Areas, ID_especialidades) VALUES (%s,%s)",
        (id_area, id_especialidad)
    )
    conexion.commit()


def insertar_profesor_bd(puntuaje, cursos, nombre):
    cursor.execute(
        "INSERT INTO Profesor (Puntuaje, Cursos, Nombre) VALUES (%s,%s,%s)",
        (puntuaje, cursos, nombre)
    )
    conexion.commit()


def insertar_materia_bd(dni_prof, id_especialidad, temas, ano):
    cursor.execute(
        """
        INSERT INTO Materia
        (DNI_profesor, ID_especialidades, Temas, Año)
        VALUES (%s,%s,%s,%s)
        """,
        (dni_prof, id_especialidad, temas, ano)
    )
    conexion.commit()


def insertar_divide_bd(id_materia, id_especialidad):
    cursor.execute(
        "INSERT INTO Divide (ID_materia, ID_especialidades) VALUES (%s,%s)",
        (id_materia, id_especialidad)
    )
    conexion.commit()


def insertar_alumno_bd(nro_alumno, nombre, mate_adeudadas):
    cursor.execute(
        """
        INSERT INTO Alumnos
        (Nro_alumno, Nombre, Mate_adeudadas)
        VALUES (%s,%s,%s)
        """,
        (nro_alumno, nombre, mate_adeudadas)
    )
    conexion.commit()


def insertar_curso_bd(id_materia, dni_alumno, promedio, turno, horarios):
    cursor.execute(
        """
        INSERT INTO Curso
        (ID_materia, DNI_alumno, Promedio, Turno, Horarios)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (id_materia, dni_alumno, promedio, turno, horarios)
    )
    conexion.commit()


def insertar_hay_bd(id_materia, nro_curso):
    cursor.execute(
        "INSERT INTO Hay (ID_materia, Nro_curso) VALUES (%s,%s)",
        (id_materia, nro_curso)
    )
    conexion.commit()


def insertar_quedan_bd(dni_alumno, nro_curso):
    cursor.execute(
        "INSERT INTO Quedan (DNI_alumno, Nro_curso) VALUES (%s,%s)",
        (dni_alumno, nro_curso)
    )
    conexion.commit()
