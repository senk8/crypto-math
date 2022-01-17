import imp


import crypto_math as gf
import pytest

@pytest.fixture
def setup():
    p = gf.get_safe_prime(1024)
    F = gf.GF(p)
    return F

def test_pow_binary(setup,benchmark):
    F = setup

    s = F.degree - 1
    g = F.generator()
    benchmark(lambda s:g**s,s)

def test_pow_windowing(setup,benchmark):
    F = setup

    s = F.degree - 1
    g = F.generator()
    f = gf.init_windowing(g,4,2**1024)
    benchmark(lambda s:f(s),s)


