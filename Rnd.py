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

	def __init__(self, maxn, idum):
		self.random_numbers = []
		self.idum = idum
		for i in range(0, maxn):
			self.random_numbers.append(self.ran())
	#		print self.idum

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
