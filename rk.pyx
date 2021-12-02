import numpy as np
cimport numpy as np
cimport cython
<<<<<<< HEAD
import math




cdef double [:] mult(double [:]  x ,double t):
       cdef:
                double [:] a = np.ones(x.shape[0])

       for i in range(x.shape[0]):
               a[i] = t*x[i]
       return np.asarray(a)



=======
from cython.parallel import prange, parallel
import math
>>>>>>> c390404d1cfb90209b0aa7eb844aea6fbe45a352

cdef class Function:

    cpdef np.ndarray evaluate(self,np.ndarray x,double t):
        return np.array([t,t,t])

cdef class rk(Function):

        cdef:
               int num_threads
               np.ndarray initial,interval

        def __init__(self,initial,interval):

                self.initial = initial
                self.interval = interval
                self.num_threads = 4

        @cython.boundscheck(False)
        @cython.wraparound(False)
        @cython.initializedcheck(False)

        cpdef solve(self,Function):
                cdef:
                        int i
                        double h
                        double [:] k1,k2,k3,k4
                        np.ndarray x,a


                x = np.linspace(self.interval[0],self.interval[1],1000)
                a = np.ones([x.shape[0],self.initial.shape[0]])
                h = x[1]-x[0]
                a[0] = self.initial

                for i in range(a.shape[0]-1):
                        k1 = Function.evaluate(a[i], x[i])
                        k2 = Function.evaluate(a[i] + mult(k1,h / 2.), x[i] + h / 2.)
                        k3 = Function.evaluate(a[i] +  mult(k2 , h / 2.), x[i] + h / 2.)
                        k4 = Function.evaluate(a[i] +  mult(k3 , h), x[i] + h)
                        a[i+1] = a[i] + (h / 6.) * (np.asarray(k1) +  mult(k2,2.) +  mult(k3,2.) +  np.asarray(k4))
                return np.vstack((x,np.transpose(a)))
