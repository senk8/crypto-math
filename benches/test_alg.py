import math_util as mu
import pytest
import galois_fields as gf


def test_padding(benchmark):
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1])
    y = F7_4([2,4,3,1])
    def f():
        if x.degree<y.degree:
            _ = mu.padding(x.coeffs,y.degree)
        else:
            _ = mu.padding(y.coeffs,x.degree)
    benchmark(f)
