import numpy as np



class deriv(object):

    def __init__(self,start):
        self.start = start

    def f1(self,x):
        return np.exp(x)

    def forward(self, dX):
        return float((self.f1(self.start+dX)-self.f1(self.start)))/dX

    def backwards(self, dX):
        return float((self.f1(self.start)-self.f1(self.start-dX)))/dX

    def center(self, dX):
        return float((self.f1(self.start+dX)-self.f1(self.start-dX)))/(2*dX)





A= deriv(0)
print("dX       forward         backwards       centered")
print("%.3g     %.3g            %.3g            %.4g" % (1, A.forward(1), A.backwards(1), A.center(1)))
print("%.3g     %.3g            %.3g            %.6g" % (0.1, A.forward(0.1), A.backwards(0.1), A.center(0.1)))
print("%.3g     %.3g            %.3g            %.9g" % (0.01, A.forward(0.01), A.backwards(0.01), A.center(0.01)))
print("%.3g     %.3g            %.3g            %.12g" % (0.001, A.forward(0.001), A.backwards(0.001), A.center(0.001)))
