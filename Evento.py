import Cuadra
import Auto
import Semaforo

class Evento:
	def __init__(self, tiempo):
		self.tiempo = tiempo

class LlegadaAuto(Evento):
	# construccion
	def __init__(self, tiempo, inicio, final):
		Evento.__init__(self, tiempo)
		self.inicio = inicio
		self.a = Auto.Auto(inicio, final)
	
	# ejecucion del evento
	def rutina(self):
		self.inicio.autos.append(self.a)

class CambioSemaforo(Evento):
	def __init__(self, tiempo, cuadra):
		Evento.__init__(self, tiempo)
		self.cuadra = cuadra
	
	def rutina():
		# Falta desarrollar esta rutina (ver Semaforo.py)
		# TODO: 
		# - Tomar la lista de autos de la cuadra, revisar la ruta (proxima cuadra),
		# hacer uso de Cuadra.agregarAuto() maximo 5 veces (numero de autos 
		# que pasan en un cambio de semaforo.
		

