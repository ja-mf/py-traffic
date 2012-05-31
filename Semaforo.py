# En terminos de implementacion, una idea es pensar que
# la clase semaforo es inutil, ya que solo manejara el estado
# del semaforo, atributo que es irrelevante mantenerlo en memoria,
# dado que, al gatillar el evento CambioSemaforo, se dejaran pasar
# una cantidad fija (o no fija) de autos hacia sus proximas calles de destino,
# donde el estado actual no interesa.

# La implementacion de la clase semaforo tomaria sentido al tener un controlador
# de semaforos, en los cuales el cambio de uno implicara necesariamente el bloqueo
# de otros.

class Semaforo:
	def __init__(self, uid, estado):
		self.uid = uid
		self.estado = bool(estado)

	def cambiarEstado(self):
		self.estado = not(self.estado)
	
