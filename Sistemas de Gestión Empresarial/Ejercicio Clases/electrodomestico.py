class Electrodomestico:
    def __init__(self, precioBase = 100, color = "blanco", consumoEnergetico = 'F', peso = 5) :
        self.__precioBase = precioBase
        self.__color = color
        self.__consumoEnergetico = consumoEnergetico
        self.__peso = peso
        
    def get_precioBase(self):
        return self.__precioBase
    
    def set_precioBase(self, precioBase):
        self.__precioBase = precioBase
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
    def get_consumoEnergetico(self):
        return self.__consumoEnergetico
    
    def set_consumoEnergetico(self, consumoEnergetico):
        self.__consumoEnergetico = consumoEnergetico
    
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso
    
    def seleccionarColor(self):
        selectColor = input("Los colores disponibles son: blanco , negro, rojo, azul y gris")
        selectColor.lower()
        
        if (selectColor != "blanco" and selectColor != "negro" and selectColor != "rojo" and selectColor != "azul" and selectColor != "gris"):
            print("Ese color no está dentro de la gama")
            selectColor = "blanco"
        else:
            self.selectColor = selectColor
    
    def comprobarConsumoEnergetico(self):
        while True:
            consumo = input("Introduce el valor energético: ").upper()
            if (consumo >= chr(65) and consumo <= chr(70)):
                self.__consumoEnergetico = self.__consumoEnergetico(chr(consumo))
                break
    
    def precioFinal(self):
        extra = self.__precioBase
        if (self.__consumoEnergetico == 'A'):
            extra += 100
        elif (self.__consumoEnergetico == 'B'):
            extra += 80
        elif (self.__consumoEnergetico == 'C'):
            extra += 60
        elif (self.__consumoEnergetico == 'D'):
            extra += 50
        elif (self.__consumoEnergetico == 'E'):
            extra += 30
        elif (self.__consumoEnergetico == 'F'):
            extra += 10
        
        if (self.__peso > 0 and self.__peso <= 19):
            extra += 10
        elif (self.__peso >= 20 and self.__peso <= 49):
            extra += 50
        elif (self.__peso >= 50 and self.__peso <= 79):
            extra += 80
        elif (self.__peso >= 80):
            extra += 100
        return extra
    
    
class Lavadora(Electrodomestico):
    def __init__(self, precioBase = 100, color = "blanco", consumoEnergetico = 'F', peso = 5, carga = 5):
        super().__init__(precioBase, color, consumoEnergetico, peso)
        self.__carga = carga

    def get_carga(self):
        return self.__carga
    
    def precioFinal(self):
        precioFinal = super().precioFinal()
        if (self.__carga >= 30):
            precioFinal += 50
        return precioFinal 
    
class Television(Electrodomestico):
    def __init__(self, precioBase = 100, color = "blanco", consumoEnergetico = 'F', peso = 5, pulgadas = 20, fourK = False):
        super().__init__(precioBase, color, consumoEnergetico, peso)
        self.__pulgadas = pulgadas
        self.__fourK = fourK
        
    def get_pulgadas(self):
        return self.__pulgadas

    def get_fourK(self):
        return self.__fourK
    
    def precioFinal(self):
        precioFinal = super().precioFinal()
        if (self.__pulgadas > 40):
            precioFinal *=  0.3
        elif (self.__fourK == True):
            precioFinal += 50
        return precioFinal
    
microondas = Electrodomestico(100, "Negro", 'F', 20)
lavadora10Kilos = Lavadora(100, "blanco", 'E', 50, 10)
tele32 = Television(250, "negro", 'F', 15, 32, False)
lista = [microondas , lavadora10Kilos, tele32]

print(microondas.precioFinal())
print(lavadora10Kilos.precioFinal())
print(tele32.precioFinal())