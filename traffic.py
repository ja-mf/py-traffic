import Auto
import Cuadra
import Evento
import Rnd
import random as r
import sys

# Tiempo de simulacion
t_sim = int(sys.argv[1])*3600
n_random = t_sim 
seed = int(sys.argv[2])
t_cambio_semaforo = int(sys.argv[3])

# Creacion de la ciudad
# Construccion de cuadras

cuadras = []

for i in range(12):
	cuadras.append(Cuadra.CuadraInicio(i))

for i in range(12,24):
	cuadras.append(Cuadra.Cuadra(i, 10))

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
# llenar la lista de eventos segun numeros formados en distribucion gamma
# con parametros k = 7.09220781, theta = 0.020051078, dado el estudio hecho.

k = 7.09220781
theta = 0.020051078

# llenar la lista de eventos segun numeros generados
listaEventos = []

# llegada de autos
t = 0
while t <= t_sim:
	random = Rnd.RandomGamma(n_random, seed, k, theta)
	#random.save_random()

	for i in random.gamma:
		if (t+i >= t_sim):
			end_cars = True
			break

		start = r.choice(cuadras[0:12])
		end = r.choice(cuadras[12:24])
		
		# si la ruta esta vacia, escojer un inicio y un final hasta que exista una.
		while not (Auto.Auto(start, end, ciudad).ruta):
			start = r.choice(cuadras[0:12])
			end = r.choice(cuadras[12:24])
		
		listaEventos.append(Evento.LlegadaAuto(t+i, start, end, ciudad))
		t = t+i	
	if end_cars: break

# cambios de semaforo
t = 0
delta = t_cambio_semaforo/3.0
while True:
	listaEventos.append(Evento.CambioSemaforo(t, cuadras[3]))
	listaEventos.append(Evento.CambioSemaforo(t+0.1, cuadras[6]))
	listaEventos.append(Evento.CambioSemaforo(t+0.2, cuadras[7]))
	listaEventos.append(Evento.CambioSemaforo(t+delta, cuadras[12]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.1, cuadras[18]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.2, cuadras[22]))
	listaEventos.append(Evento.CambioSemaforo(t+delta, cuadras[13]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.1, cuadras[17]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.2, cuadras[23]))
	listaEventos.append(Evento.CambioSemaforo(t+delta, cuadras[9]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.1, cuadras[1]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.2, cuadras[11]))
	listaEventos.append(Evento.CambioSemaforo(t+delta, cuadras[19]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.1, cuadras[15]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.2, cuadras[21]))
	listaEventos.append(Evento.CambioSemaforo(t+delta, cuadras[14]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.1, cuadras[20]))
	listaEventos.append(Evento.CambioSemaforo(t+delta+0.2, cuadras[16]))
	t += 6*delta

	if (t > t_sim): break


# simulacion: ordenar la lista de eventos por tiempo y gatillarlos
listaEventos.sort(key=lambda e: e.tiempo)

for e in listaEventos:
	e.rutina()

congestiones = 0.0
intentos = 0.0

for c in cuadras:
	if c.veces_congestionada > 0:
		print "cuadra " + str(c) + " veces_congestionada = " + str(c.veces_congestionada)
		congestiones += c.veces_congestionada
	intentos += c.intentos

print "congestiones = " + str(congestiones)
print "intentos = " + str(intentos)
print "probabilidad de taco = " + str(congestiones/intentos)

