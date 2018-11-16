import numpy as np
import matplotlib.pyplot as plt


class Graph(object):

    def __init__(self,dx,dt):
        self.dt=dt
        self.dx=dx
        self.x=np.arange(0,401,1)
        self.t=np.arange(0,3,1)
        self.v=100

    def iter(self,rho, n):
        nRho = np.zeros(401)
        for j in range(len(self.x)):
            if j ==0:
                nRho[j] = rho[j]
            elif j==401:
                nRho[j] = rho[j]
            else:
                nRho[j] = ((self.v*self.dt)/self.dx)*(rho[j-1]-rho[j])+rho[j]
        return nRho




rho=np.zeros(401)
rho[0]=1

for i in range(1,49):
    rho[i]=0.5


#print(rho)
A=Graph(1.0, 0.002)
#B=np.empty((1,1500))
B = A.iter(rho,1)
B = np.vstack((B,A.iter(B,i)))
#print(B[1])
for i in range(2,1501):
    B = np.vstack((B,A.iter(B[i-1],i)))

#print(rho)
plt.plot(A.x,rho)
plt.plot(A.x,B[500],'g')
plt.plot(A.x,B[1000],'r')
plt.plot(A.x,B[1500],'y')
plt.savefig('plot.png')
plt.show()
