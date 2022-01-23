from crypto_math import get_safe_prime, GF, init_windowing
import pytest

p = get_safe_prime(1024)

@pytest.fixture
def setup():
    F = GF(p)
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
    f = init_windowing(g,4,2**1024)
    benchmark(lambda s:f(s),s)


