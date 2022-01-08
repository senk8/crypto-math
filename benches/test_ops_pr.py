from crypto_math import GF
from crypto_math import poly_ring
import pytest

@pytest.fixture
def setup():
    F7 = GF(7)
    R7 = poly_ring(F7)
    return R7

def test_add(setup,benchmark):
    R7 = setup

    x = R7([1,1,1,1])
    y = R7([2,3,1])

    benchmark(lambda a,b:a+b,x,y)

def test_sub(setup,benchmark):
    R7 = setup

    x = R7([1,1,1,1])
    y = R7([2,3,1])

    benchmark(lambda a,b:a-b,x,y)

def test_mul(setup,benchmark):
    R7 = setup

    x = R7([1,1,1,1])
    y = R7([2,3,1])

    benchmark(lambda a,b:a*b,x,y)

def test_division(setup,benchmark):
    R7 = setup

    x = R7([1,1,1,1])
    y = R7([2,3,1])
    benchmark(R7.division,x,y)

def test_ext_euclid(setup,benchmark):
    R7 = setup
    
    x = R7([1,1,1,1])
    MOD = R7([1,0,5,4,3])

    # make sure is inverse
    benchmark(R7.ext_euclid,x,MOD)
