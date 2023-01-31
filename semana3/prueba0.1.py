"""
    prueba0.1
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 30/01/2023
    Descripcion: calcular el area y el perimetro de cualquier triangulo
"""

ladoA = float(input("Ingrese el primer P: \n"))
ladoB = float(input("Ingrese el segundo P: \n"))
ladoC = float(input("Ingrese el tercer P: \n"))
altura = float(input("Ingrese el primer A  \n"))
base = float(input("Ingrese el segunda A \n"))

perimetro = ladoA + ladoB + ladoC
area = base * altura / 2

print("el perímetro calculado del triangulo es: ",perimetro)
print("Y su área es de: ",area)
