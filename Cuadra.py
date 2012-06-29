class Cuadra(object):
	def __init__(self, uid, capacidad):
		self.uid = uid
		self.capacidad = capacidad

		self.veces_congestionada = 0
		self.intentos = 0
		self.autos = []

	def agregarAuto(self, auto):
		self.intentos += 1

		if len(self.autos) < self.capacidad:
			self.autos.append(auto)

			# sacar la cuadra anterior de la ruta
			self.autos[-1].ruta.pop(0)
			return True
		else:
			self.veces_congestionada += 1
			return False
	
	def sacarAuto(self):
		self.autos.pop(0)

class CuadraInicio(Cuadra):
	def __init__(self, uid):
		Cuadra.__init__(self, uid, 10000)
		self.capacidad = 10000
	
	def agregarAuto(self, auto):
		self.autos.append(auto)
		return True
