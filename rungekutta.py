import numpy as np

class rungekutta:
#predel  - интервал времени
#f - функция правая часть
#y0 - начальные условия
    def __init__(self,f,predel,y0):
        self.f = f
        self.y0 = y0
        self.predel = predel
        self.x = np.linspace(predel[0],predel[1],1000)

    def solve(self):
        a = np.ones([self.x.shape[0],self.y0.shape[0]])
        a[0] = self.y0
        h = self.x[1] - self.x[0]
        for i in range(a.shape[0]-1):
            k1 = self.f(a[i], self.x[i],)
            k2 = self.f(a[i] + k1 * h / 2., self.x[i] + h / 2.)
            k3 = self.f(a[i] + k2 * h / 2., self.x[i] + h / 2.)
            k4 = self.f(a[i] + k3 * h, self.x[i] + h)
            a[i+1] = a[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
        return [self.x,np.transpose(a)]
