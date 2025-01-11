CREATE TABLE Usuario (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Username VARCHAR(50) NOT NULL UNIQUE, -- Nombre de usuario
    Email VARCHAR(100) NOT NULL UNIQUE,
    Contrasena VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20) NOT NULL,
    CI VARCHAR(20) NOT NULL UNIQUE,
    Sexo CHAR(1) NOT NULL CHECK (Sexo IN ('M', 'F')), -- M para Masculino, F para Femenino
    Edad INT NOT NULL CHECK (Edad >= 0),
    Rol VARCHAR(50) NOT NULL CHECK (Rol IN ('Admin', 'Profesor', 'Tutor', 'Estudiante')) -- Restricción para roles
);

CREATE TABLE Tutor (
    ID INT PRIMARY KEY REFERENCES Usuario(ID),
    Parentesco VARCHAR(50) NOT NULL
);

CREATE TABLE Administrativo (
    ID INT PRIMARY KEY REFERENCES Usuario(ID),
    Puesto VARCHAR(50) NOT NULL
);

CREATE TABLE Estudiante (
    ID INT PRIMARY KEY REFERENCES Usuario(ID),
    RudeX VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE TutorEstudiante (
    TutorID INT NOT NULL REFERENCES Tutor(ID),
    EstudianteID INT NOT NULL REFERENCES Estudiante(ID),
    PRIMARY KEY (TutorID, EstudianteID)
);

CREATE TABLE Licencia (
    ID INT PRIMARY KEY,
    EstudianteID INT NOT NULL REFERENCES Estudiante(ID),
    TutorID INT NOT NULL REFERENCES Tutor(ID),
    FechaInicio DATE NOT NULL,
    FechaFIN DATE NOT NULL,
    Motivo VARCHAR(255) NOT NULL,
    Estado VARCHAR(50) NOT NULL CHECK (Estado IN ('Aprobada', 'Rechazada', 'Pendiente')) -- Valores válidos
);

CREATE TABLE Comportamiento (
    ID INT PRIMARY KEY,
    EstudianteID INT NOT NULL REFERENCES Estudiante(ID),
    Fecha DATE NOT NULL,
    Descripcion VARCHAR(255) NOT NULL,
    Tipo VARCHAR(50) NOT NULL CHECK (Tipo IN ('Positivo', 'Negativo')) -- Valores válidos
);

CREATE TABLE AsistenciaGeneral (
    ID INT PRIMARY KEY,
    EstudianteID INT NOT NULL REFERENCES Estudiante(ID),
    Fecha DATE NOT NULL,
    Estado VARCHAR(50) NOT NULL CHECK (Estado IN ('Presente', 'Ausente', 'Tarde')), -- Valores válidos
    HoraEntrada TIME NOT NULL,
    HoraSalida TIME
);

CREATE TABLE Curso (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Nivel VARCHAR(50) NOT NULL
);

CREATE TABLE Profesor (
    ID INT PRIMARY KEY REFERENCES Usuario(ID),
    Especialidad VARCHAR(50) NOT NULL
);

CREATE TABLE Aula (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Capacidad INT NOT NULL CHECK (Capacidad > 0), -- Capacidad debe ser positiva
    Tipo VARCHAR(50) NOT NULL,
    Ubicacion VARCHAR(255) NOT NULL
);

CREATE TABLE Materia (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    CategoriaID INT NOT NULL REFERENCES Categoria(ID)
);

CREATE TABLE Categoria (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Clases (
    ID INT PRIMARY KEY,
    IDCurso INT NOT NULL REFERENCES Curso(ID),
    IDMateria INT NOT NULL REFERENCES Materia(ID),
    IDAula INT NOT NULL REFERENCES Aula(ID),
    IDDocente INT NOT NULL REFERENCES Profesor(ID),
    Dia VARCHAR(50) NOT NULL,
    HoraInicio TIME NOT NULL,
    HoraFin TIME NOT NULL
);

CREATE TABLE AsistenciaPorClases (
    ID INT PRIMARY KEY,
    IDEstudiante INT NOT NULL REFERENCES Estudiante(ID),
    IDClase INT NOT NULL REFERENCES Clases(ID),
    Fecha DATE NOT NULL,
    Estado VARCHAR(50) NOT NULL CHECK (Estado IN ('Presente', 'Ausente', 'Tarde')),
    Hora TIME NOT NULL
);

-- Tabla para registrar el período escolar
CREATE TABLE PeriodoEscolar (
    ID INT PRIMARY KEY,
    Anio INT NOT NULL CHECK (Anio >= 2000), -- Año escolar
    Division VARCHAR(50) NOT NULL CHECK (Division IN ('Bimestral', 'Semestral', 'Trimestral')) -- División del período
);

-- Tabla para almacenar la información básica de la institución
CREATE TABLE Institucion (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Telefono VARCHAR(20),
    Email VARCHAR(100) UNIQUE
);
