import Cuadra
import Auto

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
		print "t = " + str(self.tiempo) + " llego auto!"

class CambioSemaforo(Evento):
	def __init__(self, tiempo, cuadra):
		Evento.__init__(self, tiempo)
		self.cuadra = cuadra
	
	def rutina(self):
		# TODO: 
		# - Tomar la lista de autos de la cuadra, revisar la ruta (proxima cuadra),
		# hacer uso de Cuadra.agregarAuto() con los 5 primeros autos de la lista (numero de autos 
		# que pasan en un cambio de semaforo.
		print "t = " + str(self.tiempo) + " cambio de semaforo!"

		# esto hace referencia a los ultimos 5 autos, ordenados del ultimo que lle
		for a in self.cuadra.autos[:5]:

			# el auto llego a destino
			if len(a.ruta) == 1:
				print "final auto! sacandolo"
				self.cuadra.sacarAuto()
				continue

			if a.ruta[1].agregarAuto(a):
				# si se logro agregar el auto, sacarlo de la cuadra actual
				self.cuadra.sacarAuto()
			else: 
				print "congestion en cuadra" + str(a.ruta[0])

