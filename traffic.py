import Auto
import Cuadra
import Evento
import Rnd

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

ciudad = {	cuadras[1]: [cuadras[15], 	cuadras[13]],
			cuadras[3]: [cuadras[0],	cuadras[12]],
			cuadras[6]: [cuadras[16],	cuadras[18]],
			cuadras[7]: [cuadras[19],	cuadras[22]],
			cuadras[9]: [cuadras[19],	cuadras[22]],
			cuadras[11]: [cuadras[21],	cuadras[8]],
			cuadras[12]: [cuadras[15],	cuadras[13]],
			cuadras[13]: [cuadras[2],	cuadras[4]],
			cuadras[14]: [cuadras[0],	cuadras[12]],
			cuadras[15]: [cuadras[20],	cuadras[17]],
			cuadras[16]: [cuadras[2],	cuadras[4]],
			cuadras[17]: [cuadras[14],	cuadras[5]],
			cuadras[18]: [cuadras[20],	cuadras[17]],
			cuadras[19]: [cuadras[14],	cuadras[5]],
			cuadras[20]: [cuadras[10],	cuadras[23]],
			cuadras[21]: [cuadras[16],	cuadras[18]],
			cuadras[22]: [cuadras[10],	cuadras[23]],
			cuadras[23]: [cuadras[21],	cuadras[8]]}

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


