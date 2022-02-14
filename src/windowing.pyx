# -*- coding: utf-8 -*-
#

"""
# h**l までの値を計算できる
def init_windowing(g, int h, int l): 
    cdef: 
        int b = h
        int t = l - 1
        int i 
        list gs = [ g ** (b ** i) for i in range(0, t+1) ]

    if 2 > b:
        raise ValueError('b is lower than 2')

    # t + h - 2
    def f(exp):
        cdef:
            int j, i, e
            vector[int] es = decimal_to_list_with_base(exp, b, t)
        A = g.one()
        B = A
        for j in range(h-1, 0, -1):
            for i, e in enumerate(es):
                if e == j: B *= gs[i]
            A *= B 
        return A

    return f

def windowing(exp ,int l, int b, list gs):
    cdef:
        int j, i, e
        int t = l - 1
        vector[int] es = decimal_to_list_with_base(exp, b, t)
    A = gs[0].one()
    B = A
    for j in range(b-1, 0, -1):
        for i, e in enumerate(es):
            if e == j: 
                B *= gs[i]
        A *= B 
    return A



# h**l までの値を計算できる
def init_windowing(g, p, int h, int l): 
    cdef: 
        int b = h
        int i 
        mpz_t[1024] gs 
        mpz mod = mpz(p)
        mpz base = mpz(g)
        mpz b_ = mpz(b)

    if 2 > b:
        raise ValueError('b is lower than 2')

    init_gs(gs, base, b_, mod, l)

    def f(exp):
        cdef:
            int j, i, e
            vector[int] es = encode_bit_list(mpz(exp), b, l)
            mpz res = GMPy_MPZ_New(NULL)

        helper_windowing(res, h, mod, es, gs)

        return int(res)

    return f
"""