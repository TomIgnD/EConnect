from flask import Flask, request, render_template, redirect

import database #Aca hay que importar el nombre de tu archivo Simon 

app = Flask(__name__)

# Ruta principal para mostrar la pantalla que diseñada en HTML (la que hizo Juan)
@app.route('/')
def index():
    return render_template('index.html')


# Rutas de Captura (  Para capturar todos los datos del HTML)

@app.route('/capturar_cooperadora', methods=['POST'])
def capturar_cooperadora():
    precio = request.form.get("precio_mate_x_año")
    pagos = request.form.get("pagos_pendientes")
    
    # El nombre de las funciones como esta "insertar_cooperadora_bd" es el que Simon tiene que escribir 
    # para que se puedan conectar ambos archivos, porque si le pone otro nombre no va a encontrar la funcion
    database.insertar_cooperadora_bd(precio, pagos)
    return "Datos de Cooperadora capturados. <a href='/'>Volver</a>"


@app.route('/capturar_area', methods=['POST'])
def capturar_area():
    id_coop = request.form.get("id_cooperadora")
    materias = request.form.get("materias")
    promedio = request.form.get("promedio")
    
    database.insertar_area_bd(id_coop, materias, promedio)
    return "Datos de Área capturados. <a href='/'>Volver</a>"


@app.route('/capturar_especialidad', methods=['POST'])
def capturar_especialidad():
    id_area = request.form.get("id_areas")
    cant_alum = request.form.get("cant_alum")
    turno = request.form.get("turno")
    
    database.insertar_especialidad_bd(id_area, cant_alum, turno)
    return "Datos de Especialidad capturados. <a href='/'>Volver</a>"


@app.route('/capturar_tiene', methods=['POST'])
def capturar_tiene():
    id_area = request.form.get("id_areas")
    id_especialidad = request.form.get("id_especialidades")
    
    database.insertar_tiene_bd(id_area, id_especialidad)
    return "Relación Tiene capturada. <a href='/'>Volver</a>"


@app.route('/capturar_profesor', methods=['POST'])
def capturar_profesor():
    puntuaje = request.form.get("puntuaje")
    cursos = request.form.get("cursos")
    nombre = request.form.get("nombre")
    
    database.insertar_profesor_bd(puntuaje, cursos, nombre)
    return "Datos de Profesor capturados. <a href='/'>Volver</a>"


@app.route('/capturar_materia', methods=['POST'])
def capturar_materia():
    dni_prof = request.form.get("dni_profesor")
    id_especialidad = request.form.get("id_especialidades")
    temas = request.form.get("temas")
    ano = request.form.get("ano")
    
    database.insertar_materia_bd(dni_prof, id_especialidad, temas, ano)
    return "Datos de Materia capturados. <a href='/'>Volver</a>"


@app.route('/capturar_divide', methods=['POST'])
def capturar_divide():
    id_materia = request.form.get("id_materia")
    id_especialidad = request.form.get("id_especialidades")
    
    database.insertar_divide_bd(id_materia, id_especialidad)
    return "Relación Divide capturada. <a href='/'>Volver</a>"


@app.route('/capturar_alumno', methods=['POST'])
def capturar_alumno():
    nro_alumno = request.form.get("nro_alumno")
    nombre = request.form.get("nombre")
    mate_adeudadas = request.form.get("mate_adeudadas")
    
    database.insertar_alumno_bd(nro_alumno, nombre, mate_adeudadas)
    return "Datos de Alumno capturados. <a href='/'>Volver</a>"


@app.route('/capturar_curso', methods=['POST'])
def capturar_curso():
    id_materia = request.form.get("id_materia")
    dni_alumno = request.form.get("dni_alumno")
    promedio = request.form.get("promedio")
    turno = request.form.get("turno")
    horarios = request.form.get("horarios")
    
    database.insertar_curso_bd(id_materia, dni_alumno, promedio, turno, horarios)
    return "Datos de Curso capturados. <a href='/'>Volver</a>"


@app.route('/capturar_hay', methods=['POST'])
def capturar_hay():
    id_materia = request.form.get("id_materia")
    nro_curso = request.form.get("nro_curso")
    
    database.insertar_hay_bd(id_materia, nro_curso)
    return "Relación Hay capturada. <a href='/'>Volver</a>"


@app.route('/capturar_quedan', methods=['POST'])
def capturar_quedan():
    dni_alumno = request.form.get("dni_alumno")
    nro_curso = request.form.get("nro_curso")
    
    database.insertar_quedan_bd(dni_alumno, nro_curso)
    return "Relación Quedan capturada. <a href='/'>Volver</a>"


if __name__ == '__main__':
    # Prende mi servidor local
    app.run(debug=True)
