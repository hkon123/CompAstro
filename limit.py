import numpy as np
import matplotlib.pyplot as plt



import numpy as np
import matplotlib.pyplot as plt

P_0 = 1.0
phi_in = np.repeat(P_0,401)

amp = 0.07
theta = np.arange(0.0, np.pi, np.pi/(80.0))

perturbation = amp*np.sin(theta)
phi_in[160:240] += perturbation

v_0 = 0.0
psi_in = np.repeat(v_0,len(phi_in))

def wave(xi,xf,dx,ti,tf,dt,psi_in,phi_in,cs):

    x = np.arange(xi,xf+dx,dx)
    t = np.arange(ti,tf+dt,dt)

    psi = np.empty([len(t),len(x)])
    phi = np.empty([len(t),len(x)])
    psi[0]=psi_in
    phi[0]=phi_in

    for n in range(1,len(t)):

        for j in range(0,len(x)):

            if j==len(x)-1:
                psi[n,j] = psi[n-1,j]

            else:
                psi[n,j] = psi[n-1,j]-dt*cs/dx*(phi[n-1,j+1]-phi[n-1,j])

            if j==0:
                phi[n,j] = phi[n-1,j]

            else:
                phi[n,j] = phi[n-1,j]-dt*cs/dx*(psi[n,j]-psi[n,j-1])

    return t, x, psi, phi

rho_0 = 0.75
cs = 1.0
xi = 0.0
xf = 400.0
dx = cs
ti = 0.0
tf = 140.0
dt = 1.0

t, x, psi, phi = wave(xi,xf,dx,ti,tf,dt,psi_in,phi_in,cs)

#for i in range(len(t)):

plt.plot(x,phi[0]-P_0,label=r'Initial $P-P_0$')
plt.plot(x,phi[-1]-P_0,label=r'Final $P-P_0$')
plt.plot(x,(psi[-1]-v_0)/rho_0,label='Final v',linewidth=0.5)
plt.legend()
plt.ylim(-0.05,0.08)
plt.ylabel('P,v')
plt.xlabel(r'$x/\Delta x$')
plt.title('s = '+str(dt))
plt.tight_layout()
plt.show()
    #plt.savefig('/home/Tomben/Desktop/CompAstro/Grid-based/evolution/stable_'+str(i)+'.png')
    #plt.close()

dt = 1.0001

t, x, psi, phi = wave(xi,xf,dx,ti,tf,dt,psi_in,phi_in,cs)

#for i in range(len(t)):

plt.plot(x,phi[0]-P_0,label=r'Initial $P-P_0$')
plt.plot(x,phi[-1]-P_0,label=r'Final $P-P_0$')
plt.plot(x,(psi[-1]-v_0)/rho_0,label='Final v',linewidth=0.5)
plt.ylim(-0.05,0.08)
plt.ylabel('P,v')
plt.xlabel(r'$x/\Delta x$')
plt.title('s = '+str(dt))
plt.tight_layout()
plt.show()
    #plt.savefig('/home/Tomben/Desktop/CompAstro/Grid-based/evolution/unstable_'+str(i)+'.png')
    #plt.close()
