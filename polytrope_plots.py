import matplotlib.pyplot as plt
import numpy as np

bins = 50

data = np.genfromtxt('fort.22', delimiter=' ', dtype=None, skip_header=1)

x = data[:,0]
y = data[:,1]
z = data[:,2]
h = data[:,6]
m = data[:,7]

N_total = len(x)

#m = 4*np.pi**2/N_total

'''
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
'''


def W(x,y,z,xj,yj,zj,h,v):
	
	if v==1:
		sigma = 2/3
		
	if v==2:
		sigma = 10/(7*np.pi)
		
	if v==3:
		sigma = 1/np.pi
	
	r = np.sqrt(np.power(x-xj,2)+np.power(y-yj,2)+np.power(z-zj,2))
	
	q = r/h
	
	if q <= 1:
		kernel = sigma/h**v*(1-3/2*q**2+3/4*q**3)
		
	elif q <= 2:
		kernel = sigma/h**v*(1/4*(2-q)**3)
		
	else:
		kernel = 0
		
	return kernel 

r = np.sqrt(np.power(x,2)+np.power(y,2)+np.power(z,2))

rho_all = np.empty(N_total)

for i in range(N_total):
	
	rho_all[i] = 50*m[1]/(4/3*np.pi*h[i]**3)


norm_rho = rho_all/rho_all[np.argmin(r)]

plt.scatter(r,norm_rho, marker = '.')
plt.ylabel('Density')
plt.xlabel('Radius')
plt.ylim(0,1.5)
plt.show()

rho = np.empty(N_total)

for i in range(N_total):
	
	dens = np.empty(N_total)
	
	for j in range(N_total):
		
		dr = np.sqrt(np.power(x[i]-x[j],2)+np.power(y[i]-y[j],2)+np.power(z[i]-z[j],2))
		
		dens[j] = m[j]*W(x[i],y[i],z[i],x[j],y[j],z[j],h[i],3)

			
	rho[i] = np.sum(dens)

plt.scatter(r,rho, marker = '.')
plt.ylabel('Density')
plt.ylim(0,1.5)
plt.xlabel('Radius')
plt.show()
