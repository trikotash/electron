import math
import numpy as np

def E(t,x):

    E1 = 0
    E2 = math.sin(x[0])
    E3 = 0

    return np.array([E1,E2,E3])

def H(t,x):

    H1 = 1
    H2 = 0
    H3 = 0

    return np.array([H1,H2,H3])
