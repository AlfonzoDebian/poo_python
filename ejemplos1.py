# Clase persona

class Persona:
    # Metodo constructor
    def __init__(self, nombres, apellido, edad):
        self.Nombre = nombres
        self.Apellido = apellido
        self.Edad = edad

    # Metodo para mostrar los datos de una persona
    def mostrarpersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellido)
        print("Edad: " + str(self.Edad))

# Metodo principal
def main():
    p1 = Persona("Debian", "XD", 17)
    p1.mostrarpersona()
    P2 = Persona("Didier", "XD", 88)
    P2.mostrarpersona()

    p1.Apellido = "Skibidi dark"
    p1.mostrarpersona()

if __name__ == "__main__":
    main()

