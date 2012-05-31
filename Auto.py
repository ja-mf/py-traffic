# Auto mantendra el inicio, final y la ruta
# Se hara el calculo de la ruta mediante un algoritmo y se pondra en ruta[]
# ciudad es el grafo (diccionario).

class Auto:
	def __init__(self, inicio, final):
		self.uid = 0
		self.inicio = inicio
		self.final = final
		self.ruta = []

	def calcularRuta(self, ciudad):
		self.ruta = self.ruta + [self.inicio]

#		if self.inicio == self.final:
#			return
#		if not ciudad.has_key(self.inicio):
#			return None
#		for cuadra in ciudad[self.inicio]

