import numpy as np
import math
cimport cython
from libcpp.vector cimport vector

def find_non_zero_index(seq):
    for i, x in enumerate(seq):
        if x != 0:
            return i
    return len(seq) - 1

def padding(coeffs, n, Fp=int):
    deg = len(coeffs) - 1
    if deg < n:
        return (n - deg) * (Fp(0),) + coeffs
    else:
        return coeffs

def pow_2_at_least(d):
    return 1 << len(bin(d)) - 2

def enc(poly, Range=int):
    cdef int res
    res = enc_helper(poly.coeffs, poly.degree, poly.p)
    return Range(res)

cdef inline int enc_helper(coeffs:tuple,degree:int,p:int):
    return sum([int(x)*(p**i)for i,x in zip(range(degree,-1,-1),coeffs)])

cdef inline vector[int] decimal_to_list_with_base(n, int base, int l):
    cdef: 
        int i
        vector[int] res

    res.resize(l)
    for i in range(0,l):
        res[i] = n%base
        n //= base
        if 0 >= n:
            break 

    return res

"""
def enc_into_poly(n, Range):
    coeffs = []
    while n != 0:
        coeffs.append(n % 2)
        n //= 2
    return Range(tuple(coeffs))

def enc2(poly, Range=int):
    cdef int res
    res = enc_helper(poly.coeffs, poly.degree, poly.p)
    return Range(res)

cdef inline int enc_helper2(coeffs:tuple,degree:int,p:int):
    return np.dot([ p**i for i in range(degree,-1,-1)],coeffs)


def dec(num:int,Range,p:int):
    coeffs = dec_helper(num,p)
    return Range(coeffs)

cdef vector[int] dec_helper(num:int,p:int):
    cdef:
        vector[int] coeffs

    coeffs.resize()
    while num > 0:
        coeffs = [num%p]+coeffs
        num //= p
    return coeffs
"""
