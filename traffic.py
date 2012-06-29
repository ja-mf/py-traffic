import Auto
import Cuadra
import Evento
import Rnd
import random as r

# Tiempo de simulacion
t_sim = 100

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

# Tal distribucion, nos dara la probabilidad de que llegue un auto en un periodo de tiempo.
# La distribucion inversa, dado un k y un theta definidos, con un numero aleatorio de parametro,
# nos dara entonces un periodo en el cual llega un auto.

# Para este simulador se consideraran entonces, una cantidad de autos definidos por la variable MaxAutos,
# que llegan con un periodo dado por la distribucion inversa, con el mismo recorrido :)

# generamos entonces, tantos periodos (autos) como MaxAutos

MaxAutos = 20 
seed = -127
k = 7.09220781
theta = 0.020051078

random = Rnd.RandomGamma(MaxAutos, seed, k, theta)

# llenar la lista de eventos segun numeros generados
listaEventos = []

# llegada de autos
for t in random.gamma:
	i = 1
	# periodico! cada "t" se vuelve a regenerar el evento :D
	while (t*i <= t_sim):
		# seleccionar cuadra de inicio y final de forma aleatoria (cuadras[0:12] son cuadras de inicio)
		# es probable que no exista ruta.
		# si no existe ruta, seleccionar un inicio y un final hasta que exista una.
		start = r.choice(cuadras[0:12])
		end = r.choice(cuadras[12:24])

		# si la ruta esta vacia, escojer nuevo inicio y final hasta que haya ruta
		while not (Auto.Auto(start, end, ciudad).ruta):
			start = r.choice(cuadras[0:12])
			end = r.choice(cuadras[12:24])

		listaEventos.append(Evento.LlegadaAuto(t*i, start, end, ciudad))
		i += 1

# cambios de semaforo (implementar controlador de semaforos)
t = 0
while t < t_sim:
	listaEventos.append(Evento.CambioSemaforo(t, r.choice(cuadras)))
	t += 0.5

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

