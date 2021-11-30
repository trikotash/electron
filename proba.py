import numpy as np
import math
from rk import rk,Function
from rungekutta import rungekutta
import matplotlib.pyplot as plt
import time
import math

class func(Function):
    def evaluate(self,x,t):
        return np.array([t,t,t])

def f(x,t):
    return np.array([t,t,t])

st = time.time()
k = rungekutta(f,np.array([0,10]),np.array([0,0,0]))
g = k.solve()
print(time.time() - st)

st = time.time()
k = rk(np.array([0,0,0]),np.array([0,10]))
g = k.solve(func())
print(time.time() - st)
