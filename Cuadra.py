class Cuadra(object):
	def __init__(self, uid, capacidad):
		self.uid = uid
		self.capacidad = capacidad

		self.veces_congestionada = 0
		self.intentos = 0
		self.autos = []

	def agregarAuto(self, auto):
		intentos = intentos+1

		if cantidad_autos < capacidad:
			autos.append(auto)
			return true
		else:
			return false
	
	def sacarAuto(self):
		self.autos.pop(0)

class CuadraInicio(Cuadra):
	def __init__(self, uid):
		Cuadra.__init__(self, uid, 1000)
