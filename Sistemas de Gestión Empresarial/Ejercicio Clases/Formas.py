class Punto:
    x = 0
    y = 0
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        pass
    
    def toString(self):
        return "X: " + str(self.x) + " e Y: " + str(self.y)

class Forma:
    __color = ""
    coord = Punto()
    nombre = ""
    
    def __init__(self, color = "", x= 0,y = 0,nombre = ""):
        self.coord = Punto(x,y)
        self.__color = color
        self.nombre = nombre
   
    def toString(self):
        return "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: "+ self.__color
   
    def setColor(self,color=""):
        self.__color = color
   
    def getColor(self):
        return self.__color
   
    def setCoord(self,x=0,y=0):
        self.coord = Punto(x,y)

class Rectangulo(Forma):
    lMenor = 0
    lMayor = 0
    
    def __init__(self, color="", x=0, y=0, nombre="",lMenor = 2,lMayor = 1):
        super().__init__(color, x, y, nombre)
        self.lMayor = lMayor
        self.lMenor = lMenor
        pass
    
    def toString(self):
        return super().toString() + "\nLado menor: " + str(self.lMenor) + "\nLado mayor: " +  str(self.lMayor)
    
    def area(self):
        resultado = self.lMayor * self.lMenor
        return resultado
    
    def perimetro(self):
        resultado = self.lMayor * 2 + self.lMenor * 2
        return resultado
    
    def cambiarTamanio(self,numero = 1):
        self.lMenor = self.lMenor * numero
        self.lMayor = self.lMayor * numero
        
class Elipse(Forma):
    rMayor = 0
    rMenor = 0
    PI = 3.1416

    def __init__(self, color = "", x = 0, y = 0, nombre = "",rMayor = 2, rMenor = 1):
        super().__init__(color, x, y, nombre)
        self.rMayor = rMayor
        self.rMenor = rMenor

    def toString(self):
        return super().toString() + "\nRadio Mayor: " + str(self.rMayor) +"\nRadio Menor: " + str(self.rMenor)

    def area(self):
        return self.PI * (self.rMayor * self.rMenor)

class Cuadrado(Rectangulo):

    def __init__(self, color="", x = 0, y = 0, nombre = "", lado = 1):
        super().__init__(color, x, y, nombre, lado, lado)

    def toString(self):
        return "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: "+ self.getColor() + "\nLado: " + str(self.lMayor)

class Circulo(Elipse):

    def __init__(self, color="", x=0, y=0, nombre="", radio = 1):
        super().__init__(color, x, y, nombre, radio, radio)

    def toString(self):
        return "Nombre: " + self.nombre + "\nCoordenadas: " + self.coord.toString() + "\nColor: "+ self.getColor() + "\nRadio: " + str(self.rMayor)


listaFiguras = list()
forma = Forma("negro",10,10,"Piscina")
rectangulo = Rectangulo("negro",10,10,"Piscina Olímpica",30,20)
cuadrado = Cuadrado("negro",10,10,"Ring",10)
elipse = Elipse("negro",10,10,"Circurferencia",10,9)
circulo = Circulo("negro",10,10,"Balón",7)
listaFiguras.append(forma)
listaFiguras.append(rectangulo)
listaFiguras.append(cuadrado)
listaFiguras.append(elipse)
listaFiguras.append(circulo)

for figura in listaFiguras:
    print(figura.toString())
    figura.setColor("rojo")
    figura.setCoord(20,20)
    print("")
    print(figura.toString())
    print("-----------------")