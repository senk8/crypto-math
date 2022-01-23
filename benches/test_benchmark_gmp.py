import crypto_math as gf
import pytest

def test_gmp_mod(benchmark):
    benchmark(lambda x,y:gf.gmp_mod(x,y),2**1024,2**1024)

def test_python_mod(benchmark):
    benchmark(lambda x,y:gf.gmp_mod2(x,y),2**1024,2**1024)

"""
def test_gmp(benchmark):
    benchmark(lambda x,y:gf.mul2(x,y),2**1024,2**1024)

def test_python(benchmark):
    benchmark(lambda x,y:gf.mul(x,y),2**1024,2**1024)

def test_gmp_pow(benchmark):
    benchmark(lambda g,e:gf.pow(g,e, 1000000007),2**1024,100)

def test_python_pow(benchmark):
    benchmark(lambda g,e:pow(g, e,1000000007),2**1024,100)

"""

