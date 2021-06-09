
import cmath
from numpy.lib.polynomial import poly
import pytest
import fft
import numpy as np

@pytest.mark.parametrize('m',[
    1,2,3,4,5,6,7,8,9,10
])
def test_unity(m):
    m = complex(m) 
    unity = fft.get_unity(m)
    assert cmath.isclose(unity**m,1.0+0j)

def test_dft():
    n = 8 
    m = 7
    g =(1,2,3)
    h =(2,3,2)

    actual=fft.discrete_fourier_transform(fft.padding(g,m),n)
    expect=fft.test_discrete_fourier_transform(fft.padding(g,m),n)

    assert actual==expect

def test_fft():
    g =(1,2,3)
    h =(2,3,2)

    actual=fft.fast_fourier_transform(g,h)
    expect=(2,7,14,13,6)

    assert all([ cmath.isclose(x,y) for x,y in zip(actual,expect)])
