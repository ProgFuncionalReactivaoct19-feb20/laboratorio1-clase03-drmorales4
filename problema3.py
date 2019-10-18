"""
	@drmorales4
	Problema 3:

	Dada la siguiente frase:

	"No hay medicina que cure lo que no cura la felicidad"

	Encuentre el listado que sigue:

	["No", "hay", "que", "lo", "que", "no", "la"]
"""

frase = ["No hay medicina que cure lo que no cura la felicidad"]

deFrase = lambda x: x.split()
palabras = filter(lambda y: len(deFrase))

resultado = lambda x: (palabras == 3, deFrase)

print(list(map(resultado, frase)))