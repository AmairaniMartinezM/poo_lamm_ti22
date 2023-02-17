

class Alumno:
    __nombre = None
    __matricula = None
    __carrera = None
    def __init__(self):
        print("Alumno")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
    def setCarrera(self,carrera):
        self.__carrera = carrera
    def getCarrera(self):
        return self.__carrera

amairani = Alumno()

amairani.setNombre("Amairani") 
print (amairani.getNombre())

amairani.setMatricula("1722110300") 
print (amairani.getMatricula())


amairani.setCarrera("Desarrollo de Software") 
print (amairani.getCarrera())