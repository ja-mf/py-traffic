# Auto mantendra el inicio, final y la ruta
# Se hara el calculo de la ruta mediante un algoritmo y se pondra en ruta[]
# ciudad es el grafo (diccionario).

class Auto:
	def __init__(self, inicio, final, ciudad):
		self.uid = 0
		self.inicio = inicio
		self.final = final
		self.ruta = []
		self.calcularRuta(inicio, final, ciudad)

	def calcularRuta(self, inicio, final, ciudad, ruta=[]):
		ruta = ruta + [inicio]

		# termino
		if inicio == final:
			self.ruta = ruta
			return ruta

		# no hay ruta
		if not ciudad.has_key(inicio):
			return None

		# recorrer lista de conexiones por nodo
		for nodo in ciudad[inicio]:
			if nodo not in ruta:
				ruta_n = self.calcularRuta(nodo, final, ciudad, ruta)
				if ruta_n:
					self.ruta = ruta_n
					return ruta_n

		return None
