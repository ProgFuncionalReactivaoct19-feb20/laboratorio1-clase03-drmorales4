"""
	@drmorales4
	Problema 2:

	Dada la siguiente lista:

	notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

	En contrar una lista como sigue:

	[20, 16, 20, 15]
"""

notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

suma1 = lambda x: x[0]
suma2 = lambda x: x[1]
suma3 = lambda x: x[2]

funciones = lambda x: (suma1(x) + suma2(x) + suma3 (x))

print(list(map(funciones, notas)))