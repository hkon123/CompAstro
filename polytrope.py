from polytrope_class import *
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

bins = 50
N_total = 10000
zeta_max = np.pi
delzeta = zeta_max/bins


Dist = MyPolytrope(delzeta)

zeta_1_i = Dist.distribute_box(N_total,delzeta,zeta_max)

plt.hist(zeta_1_i,bins=bins)



zeta_1 = np.arange(0,zeta_max-delzeta,0.01)

zeta_2 = zeta_1 + delzeta

N = (np.sin(zeta_2)-zeta_2*np.cos(zeta_2)-np.sin(zeta_1)+zeta_1*np.cos(zeta_1))*float(N_total)/np.pi

plt.plot(zeta_1,N)

plt.xlabel('$\zeta$')
plt.ylabel('N')
plt.show()


r = zeta_1_i
phi = np.random.uniform(size=N_total)*2*np.pi
costheta = np.random.uniform(size=N_total)*2-1

K = (2*np.pi)**2

x = r*np.sqrt(1.0-np.power(costheta,2))*np.cos(phi)
y = r*np.sqrt(1.0-np.power(costheta,2))*np.sin(phi)
z = r*costheta


plt.hist2d(x,y,bins=bins,cmap='inferno')#,vmin=0,vmax=30)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.hist2d(x,z,bins=bins,cmap='inferno')#,vmin=0,vmax=30)
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

h = np.empty(N_total)

for i in range(N_total):

	distances = np.sqrt(np.power(x-x[i],2)+np.power(y-y[i],2)+np.power(z-z[i],2))

	h[i] = np.sort(distances)[neigh-1]/2


mass = 4.0*np.pi**2/N_total

#np.savetxt('fort.22',particles)


myfile = open('fort.22', 'w')
myfile.write(str(N_total) + ' ' + str(K) + '\n')

for i in range(N_total):
	myfile.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(0.0) + ' ' + str(0.0) + ' ' + str(0.0) + ' ' + str(h[i]) + ' ' + str(mass) + '\n')
