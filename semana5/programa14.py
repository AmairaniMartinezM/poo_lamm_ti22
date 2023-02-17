"""
    programa4
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 30/01/2023
    Descripcion: Casting para convertir str en int
"""

class Persona:
    __nombre = None
    __email = None
    def __init__(self):
        print("Persona")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setEmail(self,email):
        self.__email = email
    def getEmail(self):
        return self.__email

dejah = Persona()

dejah.setNombre("Dejah") 
print (dejah.getNombre())

dejah.setEmail("correo@mascorreo.correo") 
print (dejah.getEmail())
