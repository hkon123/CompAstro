import numpy as np
import matplotlib.pyplot as plt


class diffs(object):

    def __init__(self,initial):
        self.initial = initial

    def forward(self,dt):
        yvalues = [self.initial]
        xvalues = [0]
        for i in range(12):
            yvalues.append(yvalues[-1]+(-yvalues[-1]*dt))
            xvalues.append(dt*(i+1))
        return xvalues, yvalues

    def backward(self,dt):
        yvalues = [self.initial]
        xvalues = [0]
        for i in range(12):
            yvalues.append(float(yvalues[-1])/(1+dt))
            xvalues.append(dt*(i+1))
        return xvalues, yvalues


    def center(self, dt):
        yvalues = [self.initial]
        xvalues = [0]
        for i in range(12):
            yvalues.append(float(yvalues[-1]+(-yvalues[-1]*dt/2))/(1+dt/2))
            xvalues.append(dt*(i+1))
        return xvalues, yvalues




    def real(self,dt):
        yvalues = [self.initial]
        xvalues = [0]
        for i in range(12):
            yvalues.append(np.exp(-1*(xvalues[-1]+dt)))
            xvalues.append(dt*(i+1))
        return xvalues, yvalues


    def error(self,real, comp):
        err = []
        for i in range(len(real)):
            err.append((comp[i]-real[i])/real[i])
        return err



A=diffs(1)
x, y = A.forward(0.2)
xb, yb = A.backward(0.2)
xc, yc = A.center(0.2)
xr, yr = A.real(0.2)
plt.plot(x,y)
plt.plot(xb, yb, 'r')
plt.plot(xc,yc, 'y')
plt.plot(xr,yr,'g')
plt.show()

forError = A.error(yr,y)
backError = A.error(yr,yb)
centError = A.error(yr,yc)
realError = A.error(yr,yr)

plt.plot(x,forError)
plt.plot(x,backError, 'r')
plt.plot(x,centError, 'y')
plt.plot(x,realError, 'g')
plt.show()
