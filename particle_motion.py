from clases import Ploter,Particle,ElectromagneticField
from field import E,H
import numpy as np


t = (0.,100)
init = np.array([[0,0,0],[0,0,0]])


p = Particle([E,H],init,t)
g = p.trajectory()
kap = Ploter(g[0],[g[1],g[2],g[3]],['$\omega t$',['x','y','z']])
kap = ElectromagneticField(E,H)
kap.int_plt(10.,1.)
