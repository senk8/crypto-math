import cmath
import pytest
import fft

@pytest.mark.parametrize('m',[
    1,2,3,4,5,6,7,8,9,10
])
def test_unity(m):
    m = complex(m) 
    unity = fft.get_unity(m)
    assert cmath.isclose(unity**m,1.0+0j)

@pytest.mark.parametrize('g,n',[
    ((1,2,3),8),
    ((2,3,2),8)
])
def test_dft(g,n):
    m = n-1

    actual=fft.discrete_fourier_transform(fft.padding(g,m),n)
    actual=fft.inverse_discrete_fourier_transform(actual,n)
    actual = tuple([ round((i*1/n).real) for i in actual[:len(g)]])

    assert actual == g

@pytest.mark.parametrize('g,h,expect',[
    ((1,2,3),(2,3,2),(2,7,14,13,6))
])
def test_fft(g,h,expect):
    actual=fft.fast_fourier_transform(g,h)
    assert actual==expect

'''
@pytest.mark.parametrize('g,n',[
    ((1,2,3),8),
    ((2,3,2),8)
])
def test_dft_r(g,n):
    import hoge
    m = n-1

    actual=hoge.discrete_fourier_transform(fft.padding(g,m),n)
    actual=hoge.inverse_discrete_fourier_transform(actual,n)
    actual = tuple([ round((i*1/n).real) for i in actual[5:]])

    assert actual == g

@pytest.mark.parametrize('g,h,expect',[
    ((1,2,3),(2,3,2),(2,7,14,13,6))
])
def test_fft_r(g,h,expect):
    import hoge
    actual=hoge.fast_fourier_transform(g,h)
    assert actual==expect
'''