from random import randint
from re import A


class Persona:
    def generarDNI(self):
        numero = randint(10000000, 99999999)
        letra = "TRWAGMYFPDXBNJZSQVHLCKET"
        dni = str(numero) + letra [numero % 23]
        return dni
    
    def __init__(self, nombre = "", edad = 0, sexo = '', peso = 0.0, altura = 0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = self.generarDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
    
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso):
        self.__peso = peso
    
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura):
        self.__altura = altura
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def get_sexo(self):
        return self.__sexo
    
    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def calcularIMC(self):
        imc = float(self.__peso) / pow(float(self.__altura), 2)
        if (imc > 18.5 and imc < 25):
            pesoIdeal = 0
            print("El IMC de " + self.__nombre + " es de " + str(imc))
        elif (imc < 18.5):
            pesoIdeal = -1
            print("El IMC de " + self.__nombre + " es de " + str(imc))
        else:
            pesoIdeal = 1
            print("El IMC de " + self.__nombre + " es de " + str(imc))
        return pesoIdeal
    
    def esMayorDeEdad(self):
        if (self.__edad > 18):
            esMayor = True
        else:
            esMayor = False
        return esMayor
    
    def __introducirSexo(self, char):
        if (char != 'M' and char != 'H'):
            self.__sexo = 'M'
        else:
            self.__sexo = char
        
    def toString(self):
        return "Nombre: " + self.__nombre + " Edad:" + str(self.__edad) + " DNI: " + self.__DNI + " Sexo: " + self.__sexo + " Peso: " + str(self.__peso) + " Altura: " + str(self.__altura)
    
nombre = input("Introduce el nombre: ")
edad = input("Introduce la edad: ")
sexo = input("Introduce el sexo: ")
peso = input("Introduce el peso: ")
altura = input("Introduce la altura: ")
    
persona1 = Persona (nombre, edad, sexo, peso, altura)

persona2 = Persona(nombre, edad, sexo)

antonio = Persona()   
antonio.set_nombre("Antonio")
antonio.set_edad(20)
antonio.set_sexo('H')
antonio.set_peso(60)
antonio.set_altura(1.60)

print(antonio.toString())
print(antonio.calcularIMC())
print(antonio.esMayorDeEdad())

print(persona1.toString())
print(persona1.calcularIMC())
print(persona1.esMayorDeEdad())

print(persona2.toString())
print(persona2.calcularIMC())
print(persona2.esMayorDeEdad())