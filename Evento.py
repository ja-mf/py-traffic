import Cuadra
import Auto
import Semaforo

class Evento:
	def __init__(self, tiempo):
		self.tiempo = tiempo

class LlegadaAuto(Evento):
	# construccion
	def __init__(self, tiempo, inicio, final, ciudad):
		Evento.__init__(self, tiempo)
		self.inicio = inicio
		self.a = Auto.Auto(inicio, final, ciudad)
	
	# ejecucion del evento
	def rutina(self):
		self.inicio.autos.append(self.a)
		print "llego auto!"

class CambioSemaforo(Evento):
	def __init__(self, tiempo, cuadra):
		Evento.__init__(self, tiempo)
		self.cuadra = cuadra
	
	def rutina(self):
		# Falta desarrollar esta rutina (ver Semaforo.py)
		# TODO: 
		# - Tomar la lista de autos de la cuadra, revisar la ruta (proxima cuadra),
		# hacer uso de Cuadra.agregarAuto() maximo 5 veces (numero de autos 
		# que pasan en un cambio de semaforo.
		print "cambio de semaforo!"
#		for a in self.cuadra.autos:i
#			if a.inicio.
