class Course:
    nombre_materia = "POO"
    programa = "semiescolarizado"
    numero_alumnos = "6"
    docente = "Martin Avila"
    codigo_materia = "11111"
    numero_de_examen = "2"
    def __init__(self, nombre_materia, codigo_materia, programa, numero_alumnos,docente, numero_de_examen):
        self.nombre_materia = nombre_materia
        self.codigo_materia = codigo_materia
        self.programa = programa
        self.numero_alumnos = numero_alumnos
        self.docente = docente
        self.numero_de_examen = numero_de_examen


MD = Course("Matematicas Discretas", "42590", "Semiescolarizado", 8)
DW = Course("Desarrollo Web", "31339", "Escolarizado", 20)
MB = Course("Matematicas Basicas", "12456", "Impulso", 11)
def datos_curso_impulso(MD):
    print("Los datos del curso de impulso que quiere consultar son: " + MD.nombre_materia + ", codigo de la materia: " + MD.codigo_materia + ", programa: " + MD.programa + ".")

def datos_curso_matutino(DW):
    print("Los datos del curso del turno de la mañana que quiere consultar son: " + DW.nombre_materia + ", codigo de la materia: " + DW.codigo_materia + ", programa: " + DW.programa + ".")

def datos_curso_MB(MB):
    print("Los datos del curso que solicita son: " + MB.nombre_materia + ", codigo de la materia: " + MB.codigo_materia + ", programa: " + MB.programa + ".")

datos_curso_impulso(MD)
datos_curso_matutino(DW)
datos_curso_MB(MB)

def nombre_materia():
    print("La materia: " + Course.nombre_materia + " tiene " + Course.numero_alumnos + " alumnos.")

def programa():
    print("La materia: " + Course.nombre_materia + " es del turno nocturno y pertenece al programa: " + Course.programa + ".")

def docente():
    print("El maestro: " + Course.docente + " tiene " + Course.numero_alumnos + " tesistas.")
nombre_materia()
programa()
docente()