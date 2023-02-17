"""
    programa10
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 8/02/2023
    Descripcion:
"""
def mayor(numero1, numero2):  #  definición de función usa dapara crear objetos, las cuales son definidas por cada usuario

	if numero1>numero2: # ejecutar un bloque de código si, y solo si, se cumple una determinada condición
		print(numero1) # mostrar texto en pantalla

	elif numero2>numero1: # Enlaza condiciones
	 	print(numero2) # mostrar texto en pantalla
	else: # combinar la ejecución de la condición y la iteración
		print("iguales") # mostrar texto en pantalla

mayor(3,2)#3 call

mayor(2,3)#3

mayor(3,3)#None