"""
    prueba0.1
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 30/01/2023
    Descripcion:Calcular el area y el perimetro de cualquier triangulo
"""

lado_1 = float(input("Ingrese el lado 1: \n"))   #leer el perimetro de un triangulo
lado_2 = float(input("Ingrese el lado 2 : \n"))  #leer el perimetro de un triangulo
lado_3 = float(input("Ingrese el lado 3: \n"))  #leer el perimetro de un triangulo
altura = float(input("Ingrese el altura  \n"))  #leer la altura de un triangulo


perimetro = lado_1 + lado_2 + lado_3 #calcular el perimetro 
area = lado_1 * altura / 2   #calcular el area 

print("el perímetro calculado del triangulo es:",perimetro)   #resultado del perimetro 
print("Y su área es de:",area)    #resultado del area
 