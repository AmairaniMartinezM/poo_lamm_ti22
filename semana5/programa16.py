"""
    programa16
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 15/02/23
    Descripcion: Clase profesor
"""
from Persona import Persona

class Profesor(Persona): # Crear la clase Profesor del archivo persona .py
    def __init__(self) -> None:  # definicion creada porcualquier usuario
        super().__init__() # Llama al constructor de la clase persona
        print("Profesor")  # mostrar texto en pantalla

objeto_profesor = Profesor() # Crea un objeto de la clase Profesor