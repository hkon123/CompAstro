import numpy as np

class MyPolytrope:

	#define class and its properties
	#in this case we need only lifetime tau

	def __init__(self, delzeta):

		self.delzeta = delzeta


	#produce a random decay time t in range from 0 to when the probability is 0.001%
	#we assume that decay happening afterwards is unlikely
	#even though P<0.1% is unlikely there can be still some decay happening at lower probabilities
	#with relatively high value increasing the mean value of t_i

	def give(self,zeta_max):

		zeta_1 = np.random.uniform()*zeta_max
		return zeta_1


	#calculate probability of decay P at time t

	def N(self,zeta_1,Ntotal,delzeta):	

		zeta_2 = zeta_1 + delzeta
		Nvalue = (np.sin(zeta_2)-zeta_2*np.cos(zeta_2)-np.sin(zeta_1)+zeta_1*np.cos(zeta_1))/np.pi*Ntotal
		return Nvalue

	
	#distribute decay times according to the exponential law using box method until we have 'number' of decay times
	
	def distribute_box(self,Ntotal,delzeta,zeta_max):

		zeta_1_all = np.zeros(Ntotal)

		for i in range(Ntotal):
			
			while True:
				zeta_1_all[i] = self.give(zeta_max)
				y = np.random.uniform()*Ntotal
			
				if y <= self.N(zeta_1_all[i],Ntotal,delzeta):
						break


		return zeta_1_all
