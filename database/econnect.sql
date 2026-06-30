PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Cooperadora (
    ID_cooperadora INTEGER PRIMARY KEY AUTOINCREMENT,
    Precio_mate_x_anio INTEGER,
    Pagos_pendientes INTEGER
);

CREATE TABLE IF NOT EXISTS Areas (
    ID_Areas INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_cooperadora INTEGER,
    Materias TEXT,
    Promedio REAL,
    FOREIGN KEY (ID_cooperadora)
        REFERENCES Cooperadora(ID_cooperadora)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Especialidades (
    ID_especialidades INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Areas INTEGER,
    Cant_alum INTEGER,
    Turno TEXT,
    FOREIGN KEY (ID_Areas)
        REFERENCES Areas(ID_Areas)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Tiene (
    ID_Areas INTEGER,
    ID_especialidades INTEGER,
    PRIMARY KEY (ID_Areas, ID_especialidades),
    FOREIGN KEY (ID_Areas)
        REFERENCES Areas(ID_Areas)
        ON DELETE CASCADE,
    FOREIGN KEY (ID_especialidades)
        REFERENCES Especialidades(ID_especialidades)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Profesor (
    DNI_profesor INTEGER PRIMARY KEY,
    Puntuaje TEXT,
    Cursos TEXT,
    Nombre TEXT
);

CREATE TABLE IF NOT EXISTS Materia (
    ID_materia INTEGER PRIMARY KEY AUTOINCREMENT,
    DNI_profesor INTEGER,
    ID_especialidades INTEGER,
    Temas TEXT,
    Anio INTEGER,
    FOREIGN KEY (DNI_profesor)
        REFERENCES Profesor(DNI_profesor)
        ON DELETE CASCADE,
    FOREIGN KEY (ID_especialidades)
        REFERENCES Especialidades(ID_especialidades)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Divide (
    ID_materia INTEGER,
    ID_especialidades INTEGER,
    PRIMARY KEY (ID_materia, ID_especialidades),
    FOREIGN KEY (ID_materia)
        REFERENCES Materia(ID_materia)
        ON DELETE CASCADE,
    FOREIGN KEY (ID_especialidades)
        REFERENCES Especialidades(ID_especialidades)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Alumnos (
    DNI_alumno INTEGER PRIMARY KEY,
    Nro_alumno INTEGER,
    Nombre TEXT,
    Mate_adeudadas TEXT
);

CREATE TABLE IF NOT EXISTS Curso (
    Nro_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_materia INTEGER,
    DNI_alumno INTEGER,
    Promedio REAL,
    Turno TEXT,
    Horarios TEXT,
    FOREIGN KEY (ID_materia)
        REFERENCES Materia(ID_materia)
        ON DELETE CASCADE,
    FOREIGN KEY (DNI_alumno)
        REFERENCES Alumnos(DNI_alumno)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Hay (
    ID_materia INTEGER,
    Nro_curso INTEGER,
    PRIMARY KEY (ID_materia, Nro_curso),
    FOREIGN KEY (ID_materia)
        REFERENCES Materia(ID_materia)
        ON DELETE CASCADE,
    FOREIGN KEY (Nro_curso)
        REFERENCES Curso(Nro_curso)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Quedan (
    DNI_alumno INTEGER,
    Nro_curso INTEGER,
    PRIMARY KEY (DNI_alumno, Nro_curso),
    FOREIGN KEY (DNI_alumno)
        REFERENCES Alumnos(DNI_alumno)
        ON DELETE CASCADE,
    FOREIGN KEY (Nro_curso)
        REFERENCES Curso(Nro_curso)
        ON DELETE CASCADE
);