class Persona:
    def __init__(self, nombre="", apellidos="", edad=0):
        self.__Nombre = nombre
        self.__Apellidos = apellidos
        self.__Edad = edad

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    def MostrarPersona(self):
        print("Nombre:", self.__Nombre)
        print("Apellidos:", self.__Apellidos)
        print("Edad:", self.__Edad)

class Alumno(Persona):
    def __init__(self, nombre="", apellidos="", edad=0, curso="", asignaturas=None):
        super().__init__(nombre, apellidos, edad)
        self.__Curso = curso
        self.__Asignaturas = asignaturas if asignaturas is not None else []
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        super().MostrarPersona()
        print("Curso:", self.__Curso)
        print("Matrículas:", self.__Asignaturas)

class Profesor(Persona):
    def __init__(self, nombre="", apellidos="", edad=0, antiguedad=0, tutorias=None, telefono=""):
        super().__init__(nombre, apellidos, edad)
        self.__Antiguedad = antiguedad
        self.__Tutorias = tutorias if tutorias is not None else []
        self.__Telefono = telefono
    
    def getAntiguedad(self):
        return self.__Antiguedad
    
    def setAntiguedad(self, antiguedad):
        self.__Antiguedad = antiguedad

    def getTutorias(self):
        return self.__Tutorias
    
    def setTutorias(self, tutorias):
        self.__Tutorias = tutorias

    def getTelefono(self):
        return self.__Telefono
    
    def setTelefono(self, telefono):
        self.__Telefono = telefono

    def mostrarProfesor(self):
        print("Profesor")
        super().MostrarPersona()
        print("Antigüedad:", self.__Antiguedad)
        print("Tutorías:", self.__Tutorias)
        print("Teléfono:", self.__Telefono)

def main():
    alumno = Alumno("Néstor", "Páez Sarmiento", 25, "Bachillerato", ["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()

    profesor = Profesor("Juan", "Pérez", 45, 15, ["Lunes 10-12", "Miércoles 14-16"], "123-456-7890")
    profesor.mostrarProfesor()

if __name__ == "__main__":
    main()