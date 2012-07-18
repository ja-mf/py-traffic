import math

class RandomGamma:
	# Constants related with random number generator function ran. 
	# Got from "Numerical recipes in C"
	IA = 16807
	IM = 2147483647
	AM = (1.0/IM)
	IQ = 127773
	IR = 2836
	NTAB = 32
	NDIV = (1+(IM-1)/NTAB)
	EPS = 1.2e-7
	RNMX = (1.0-EPS)
	
	iy = 0
	iv = [None]*NTAB
	idum = -275920
	
	# save generated numbers	
	def save_random(self):
		f = open('random_gamma_generated', 'a')
		for i in self.gamma:
			f.write(str(i) + "\n")
		f.close
	
	# maxn: cantidad de numeros a generar
	# idum: seed
	# Gamma(k = alpha, theta = beta)
	def __init__(self, maxn, idum, alpha, beta):
		# idum es la semilla comun
		self.idum = idum
		# self.gamma son los numeros generados en distribucion gamma, segun alpha y beta.
		self.gamma = []

		# se procedera a aplicar el algoritmo aparecido
		# en la pagina 464. calulando constantes
		a = 1/math.sqrt(2*alpha-1)
		b = alpha - math.log(4)
		q = alpha + 1/a
		theta = 4.5
		d = 1 + math.log(theta)
		
		while (len(self.gamma) < maxn):
			# U1 y U2 son dos numros aleatorios
			# pertenecientes a una distribucion uniforme entre 0 y 1.
			U1 = self.ran()
			U2 = self.ran()

			V = a*math.log(U1/(1-U1))
			Y = alpha*math.exp(V)
			Z = math.pow(U1, 2)*U2
			W = b + q*V - Y

			if (W + d - theta*Z >= 0):
				self.gamma.append(Y)
			elif (W >= math.log(Z)):
				self.gamma.append(Y)
			else:
				continue

	def ran(self):

		if (self.idum <= 0) or (not(self.iy)):
	#		print "init"
			if -self.idum < 1: 	self.idum = 1
			else: self.idum = -self.idum

			for j in reversed(range(0, self.NTAB+7)):
				k = self.idum / self.IQ
				self.idum = self.IA*(self.idum - k*self.IQ) - self.IR*k

				if self.idum < 0: self.idum += self.IM

				if j < self.NTAB: self.iv[j] = self.idum

			self.iy = self.iv[0]

	#	print "not initializing"
		k = self.idum/self.IQ
		self.idum = self.IA*(self.idum-k*self.IQ)-self.IR*k
		
		if self.idum < 0:
			self.idum += self.IM

		j = self.iy/self.NDIV
		self.iy = self.iv[j]
		self.iv[j] = self.idum

		temp = self.AM*self.iy
		if temp > self.RNMX: 
			return self.RNMX
		else:
			return temp

