"""
	@drmorales4
	Problema 1:

	Dado el siguiente conjunto de promedios de estudiantes; determinar los estudiantes que pasan de ciclo.
	Todos los estudiantes que pasan de ciclo son aquellos que tienen un promedio de 16.5 o mayor.

	promedios.txt
"""
archivo = open("promedios.txt")
x = archivo.read()
list(x)

resultado = filter(lambda x: x >= 16.5 , archivo)
print(resultado)
print(list (resultado))