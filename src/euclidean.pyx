import numpy as np
import math
from libcpp.vector cimport vector

cdef (int,int) determine_m_n(list xs):
    cdef:
        int m, n
         
    ys = np.array(xs)
    m, n = ys.argsort()[-2:][::-1]
    return m, n

def init_euclidean(g, int h, int l):
    cdef:
        int b, i
        list gs

    b = h
    gs = [ g ** (b ** i) for i in range(0, l) ]

    if 2 > b:
        raise ValueError('b is lower than 2')

    def f(e):
        cdef:
            int q, m, n
            list gsd
            vector[int] es = decimal_to_list_with_base(e, b, l-1)
            list xs

        gsd = gs[:]
        xs = es
        m, n = determine_m_n(xs)
        while xs[n]!=0:
            q = math.floor(xs[m] / xs[n])
            gsd[n] = (gsd[m] ** q) * gsd[n]
            xs[m] = xs[m] % xs[n]
            m, n = determine_m_n(xs)
        return gsd[m] ** xs[m]

    return f