import Auto
import Cuadra
import Evento

# Tiempo de simulacion
t_sim = 50

# Creacion de la ciudad

# Construccion de cuadras

cuadras = []

for i in range(12):
	cuadras.append(Cuadra.CuadraInicio(i))

for i in range(12,24):
	cuadras.append(Cuadra.Cuadra(i, 20))

# Conexion de cuadras

# implementar diccionario para las conexiones entre cuadras (grafo)
# (ver http://www.python.org/doc/essays/graphs/)

ciudad = {cuadras[0]: [cuadras[12]],
		  cuadras[12]: [cuadras[13], cuadras[14]]}

# Lista de eventos
# tiempo, inicio y final
listaEventos = [Evento.LlegadaAuto(2, cuadras[0], cuadras[13], ciudad), 
				Evento.LlegadaAuto(5, cuadras[0], cuadras[14], ciudad),
				Evento.CambioSemaforo(6, cuadras[1])]


# Inicio de la simulacion
for t in range(t_sim):

	# Recorrer lista de eventos
	for e in listaEventos:
		# Hay algun evento en el tiempo t?
		if e.tiempo == t:
			# Gatillar evento
			e.rutina()


# debug
# print cuadras[0].autos[0].final


