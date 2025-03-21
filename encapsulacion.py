

# Clase coordenada



class Coordenada:


    def _init_(self, x, y):
        self.__X = x , self.__Y = y
    
    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def setX(self, x):
        self.__X = x

    def SetY(self, y):
        self.__Y = y
    
    def mostrarCoordenada(self):
        print("(", self.__X, "and", self.__Y, ")")


class Cuadrado:

    def _init_(self, v1, v2, v3, v4):

        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    def __mostrarCoordenadaV1(self):
        print("(", self.__V1.getX(), "and", self.__V1.getY(),")")
    
    def __mostrarCoordenadaV2(self):
        print("(", self.__V2.getX(), "and", self.__V2.getY(),")")
    
    def __mostrarCoordenadaV3(self):
        print("(", self.__V3.getX(), "and", self.__V3.getY(),")")
    
    def __mostrarCoordenadaV4(self):
        print("(", self.__V4.getX(), "and", self.__V4.getY(),")")
    


    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguentes vertice. ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()

def main():
    x1 = int(input("Valor de x: "))
    x2 = int(input("Valor de y: "))

    c1 = Coordenada(x1, x2)
    c1.mostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    Cuadrado1 = Cuadrado(v1, v2, v3, v4)
    Cuadrado1.mostrarVertices()
    
    