import numpy as np
cimport numpy as np
cimport cython
from cython.parallel import prange, parallel

cdef class Cython_Class:
    cdef:
        int m1, n1, m2, n2, num_threads
        double [:] args, funcs, init, interval
        double [:, :] result
        np.ndarray mat3


    def __init__(self, m1, m2,init):
        self.args = m1
        self.funcs = m2
        self.quant = m2.shape[0]
        self.mat3 = np.zeros((self.m1, self.n2))
        self.mat3_mv = self.mat3
        self.num_threads = 4

    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.initializedcheck(False)
    cpdef solve(self):
        cdef int i, j, k, nthreads
        cdef double h
        cdef double [:,:] k1,k2,k3
        h = self.args[1] - self.args[0]
        with nogil:
            nthreads = self.num_threads
            for i in prange(self.funcs.shape[0]-1, num_threads=nthreads):
              k1 = self.f(a[i], self.x[i],)
              k2 = self.f(a[i] + k1 * h / 2., self.x[i] + h / 2.)
              k3 = self.f(a[i] + k2 * h / 2., self.x[i] + h / 2.)
              k4 = self.f(a[i] + k3 * h, self.x[i] + h)
              a[i+1] = a[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
