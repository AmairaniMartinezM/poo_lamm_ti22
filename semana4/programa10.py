"""
    programa10
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 8/02/2023
    Descripcion:Programa que por medio de un def nosdelnumero mayor de dos  numeros version 2
"""
def mayor(numero1:int,numero2:int)->int: #  definición de función usa dapara crear objetos, las cuales son definidas por cada usuario
	mayor = None # denota falta de valor
	if numero1>numero2: # ejecutar un bloque de código si, y solo si, se cumple una determinada condición
		mayor = numero1
	elif numero2>numero1: # Enlaza condiciones
		mayor = numero2
	else:  # combinar la ejecución de la condición y la iteración
		mayor = None # denota falta de valor
	return mayor  #  final de la función y continúa la ejecución del programa tras la llamada a la función
print(mayor(3,2))	# mostrar texto en pantalla
print(mayor(2,3))	# mostrar texto en pantalla
print(mayor(3,3))	# mostrar texto en pantalla
        