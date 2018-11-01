import matplotlib.pyplot as plt
import numpy as np
import random

bins = 50
Emax = np.pi
De = Emax/bins
Ntot = 10000
datay = []
datax = []

class poly(object):

    def Funk(self,E1,E2,N):
        return (np.sin(E2)-E2*np.cos(E2)-np.sin(E1)+E1*np.cos(E1))*float(N)/np.pi

    def binning(self, ycoords, xcoords, De, Emax, bins):
        distrange =[]
        temp = De
        for i in range(bins):
            distrange.append(temp)
            temp += De
        bindist = []
        count1 = 0
        count2 = 0
        for i in range(5):
            ycoords = np.append(ycoords,ycoords)
            xcoords = np.append(xcoords,xcoords)
        for i in range(len(ycoords)):
            count1+=1
            for j in distrange:
                if xcoords[i]< j:
                    count2+=1
                    bindist.append(j)
                    break
                else:
                    continue
        return bindist, count1, count2


    def MC(self,ycoords,xcoords,Emax, De, N):
        self.dist = np.zeros(10000)
        for i in range(10000):
            while True:
                varx = random.uniform(0, Emax-De)
                vary = random.uniform(0,np.amax(ycoords)+100)
                if self.Funk(varx, varx+De, N) >=vary:
                    self.dist[i] = varx
                    break



a=poly()
E1 = np.arange(0,Emax-De,0.01)
E2 = E1 + De
#print(len(E1))
dist = a.Funk(E1,E2,Ntot)

#binned, count1, count2 = binning(dist,E1,De,Emax,bins)
#print(count1)
#print(count2)

a.MC(dist,E1,Emax,De,Ntot)


plt.plot(E1,dist)
#n, bins, patches =
plt.hist(a.dist, bins)#, normed=1)
plt.show()


r = a.dist
phi = np.random.uniform(size=Ntot)*2*np.pi
costheta = np.random.uniform(size=Ntot)*2-1

K = (2*np.pi)**2

x = r*np.sqrt(1.0-np.power(costheta,2))*np.cos(phi)
y = r*np.sqrt(1.0-np.power(costheta,2))*np.sin(phi)
z = r*costheta


plt.hist2d(x,y,bins=bins,cmap='inferno')#,vmin=0,vmax=30)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.hist2d(x,z,bins=bins,cmap='magma')#,vmin=0,vmax=30)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('z')
plt.show()

plt.hist2d(y,z,bins=bins,cmap='inferno')#,vmin=0,vmax=30)
plt.colorbar()
plt.xlabel('y')
plt.ylabel('z')
plt.show()

neigh = 50

h = np.empty(Ntot)

for i in range(Ntot):

	distances = np.sqrt(np.power(x-x[i],2)+np.power(y-y[i],2)+np.power(z-z[i],2))

	h[i] = np.sort(distances)[neigh-1]/2


mass = 4.0*np.pi**2/Ntot




myfile = open('fort.22', 'w')
myfile.write(str(Ntot) + ' ' + str(K) + '\n')

for i in range(Ntot):
	myfile.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(0.0) + ' ' + str(0.0) + ' ' + str(0.0) + ' ' + str(h[i]) + ' ' + str(mass) + '\n')
