import numpy as np
import math

def determine_m_n(xs):
    ys = np.array(xs)
    return ys.argsort()[-2:][::-1]

def init_euclidean(g, h, l):
    b = h
    gs = [ g ** (b ** i) for i in range(0, l) ]

    if 2 > b:
        raise ValueError('b is lower than 2')

    def f(e):
        es = decimal_to_list_with_base(e, b, l-1)
        xs = es
        m, n = determine_m_n(xs)
        while xs[n]!=0:
            q = math.floor(xs[m] / xs[n])
            gs[n] = (gs[m] ** q) * gs[n]
            xs[m] = xs[m] % xs[n]
            m, n = determine_m_n(xs)
        return gs[m] ** xs[m]

    return f