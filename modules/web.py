from flask import Flask, request, render_template, redirect
import os

from . import database

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/administrador")
def administrador():
    return render_template("vista_Administrador.html")


@app.route('/capturar_cooperadora', methods=['POST'])
def capturar_cooperadora():

    precio = request.form.get("precio_mate_x_anio")
    pagos = request.form.get("pagos_pendientes")

    database.insertar_cooperadora_bd(precio, pagos)

    return redirect("/")


@app.route('/capturar_area', methods=['POST'])
def capturar_area():

    id_coop = request.form.get("id_cooperadora")
    materias = request.form.get("materias")
    promedio = request.form.get("promedio")

    database.insertar_area_bd(id_coop, materias, promedio)

    return redirect("/")


@app.route('/capturar_especialidad', methods=['POST'])
def capturar_especialidad():

    id_area = request.form.get("id_areas")
    cant_alum = request.form.get("cant_alum")
    turno = request.form.get("turno")

    database.insertar_especialidad_bd(id_area, cant_alum, turno)

    return redirect("/")


@app.route('/capturar_tiene', methods=['POST'])
def capturar_tiene():

    id_area = request.form.get("id_areas")
    id_especialidad = request.form.get("id_especialidades")

    database.insertar_tiene_bd(id_area, id_especialidad)

    return redirect("/")


@app.route('/capturar_profesor', methods=['POST'])
def capturar_profesor():

    dni = request.form.get("dni_profesor")
    puntuaje = request.form.get("puntuaje")
    cursos = request.form.get("cursos")
    nombre = request.form.get("nombre")

    database.insertar_profesor_bd(
        dni,
        puntuaje,
        cursos,
        nombre
    )

    return redirect("/")


@app.route('/capturar_materia', methods=['POST'])
def capturar_materia():

    dni_prof = request.form.get("dni_profesor")
    id_especialidad = request.form.get("id_especialidades")
    temas = request.form.get("temas")
    anio = request.form.get("anio")

    database.insertar_materia_bd(
        dni_prof,
        id_especialidad,
        temas,
        anio
    )

    return redirect("/")


@app.route('/capturar_divide', methods=['POST'])
def capturar_divide():

    id_materia = request.form.get("id_materia")
    id_especialidad = request.form.get("id_especialidades")

    database.insertar_divide_bd(id_materia, id_especialidad)

    return redirect("/")


@app.route('/capturar_alumno', methods=['POST'])
def capturar_alumno():

    dni = request.form.get("dni_alumno")
    nro_alumno = request.form.get("nro_alumno")
    nombre = request.form.get("nombre")
    mate_adeudadas = request.form.get("mate_adeudadas")

    database.insertar_alumno_bd(
        dni,
        nro_alumno,
        nombre,
        mate_adeudadas
    )

    return redirect("/")


@app.route('/capturar_curso', methods=['POST'])
def capturar_curso():

    id_materia = request.form.get("id_materia")
    dni_alumno = request.form.get("dni_alumno")
    promedio = request.form.get("promedio")
    turno = request.form.get("turno")
    horarios = request.form.get("horarios")

    database.insertar_curso_bd(
        id_materia,
        dni_alumno,
        promedio,
        turno,
        horarios
    )

    return redirect("/")


@app.route('/capturar_hay', methods=['POST'])
def capturar_hay():

    id_materia = request.form.get("id_materia")
    nro_curso = request.form.get("nro_curso")

    database.insertar_hay_bd(id_materia, nro_curso)

    return redirect("/")


@app.route('/capturar_quedan', methods=['POST'])
def capturar_quedan():

    dni_alumno = request.form.get("dni_alumno")
    nro_curso = request.form.get("nro_curso")

    database.insertar_quedan_bd(dni_alumno, nro_curso)

    return redirect("/")