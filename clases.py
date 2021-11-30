import numpy as np
import math
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cbook as cbook
from matplotlib import cm




class ElectromagneticField:
    def __init__(self,E,H):
        self.E = E
        self.H = H

    def ElectricField(self,x,t):
        return self.E(t,x)

    def MagneticField(self,x,t):
        return self.H(t,x)

    def Intencity(self,x,t):
        I = np.dot(self.E(t,x),self.E(t,x)) + np.dot(self.H(t,x),self.H(t,x))
        return I/(4*math.pi)

    def int_plt(self,a,t):
        x = np.linspace(-a,a,100)
        a = np.dot(self.E(t,x),self.E(t,x)) + np.dot(self.H(t,x),self.H(t,x))
        fig, ax = plt.subplots()
        pcm = ax.pcolor(x, x, a/(4*math.pi), vmin=-1., vmax=1., cmap='RdBu_r'
        ,shading='auto')
        plt.show()


class Particle:
    def __init__(self,field,intial_conditions,time_interval):
        self.field = field
        self.intial_momentum = intial_conditions[1]
        self.intial_coordinate = intial_conditions[0]
        self.time_interval = time_interval


    def trajectory(self):
        def right_sight(t,arg):


            p = np.hsplit(arg,2)[0]
            x = np.hsplit(arg,2)[1]
            E = self.field[0](t,x)
            H = self.field[1](t,x)
            fp = -E-np.cross(p,H)/(math.sqrt(1.+math.sqrt(np.dot(p,p))))
            fx = p/(math.sqrt(1.+math.sqrt(np.dot(p,p))))
            return np.hstack((fp,fx))

        t0 = self.time_interval
        y0 = np.hstack((self.intial_momentum,self.intial_coordinate))
        a = solve_ivp(right_sight,t0 ,y0,t_eval=np.linspace(self.time_interval[0],
        self.time_interval[1],10000))

        coordinate1 = a.y
        time = a.t
        k = time.shape[0]+1
        x = a.y[3]
        y = a.y[4]
        z = a.y[5]


        return [time,x,y,z]

class Ploter:
    def __init__(self,abscissa,ordinate,legend):
        self.abscissa = abscissa
        self.ordinate = ordinate
        self.legend = legend

    def time_plot(self):
        fig, ax = plt.subplots()
        for i in range(len(self.ordinate)):
            plt.plot(self.abscissa,self.ordinate[i],label = self.legend[1][i])
        ax.set_xlabel(self.legend[0])
        plt.grid()
        plt.legend()
        plt.show()

    def three_dim_plot(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        z = self.ordinate[2]
        y = self.ordinate[1]
        x = self.ordinate[0]
        ax.plot3D(x,y,z,'red')
        plt.show()
