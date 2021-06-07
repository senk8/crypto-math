from galois_fields import GF
from poly_ring import poly_ring
import pytest

@pytest.fixture
def setup():
    F7 = GF(7)
    R7 = poly_ring(F7)
    return R7

@pytest.mark.parametrize('x,y,expect',[
    ([1,1,1,1],[2,3,1],[1,3,4,2]),
    ([2,3,1],[6,1,3,1],[6,3,6,2]),
    ([1,1,1,1],[6,1,3,1],[2,4,2]),
])
def test_add(setup,x,y,expect):
    R7 = setup

    x = R7(x)
    y = R7(y)

    assert x+y == R7(expect)

@pytest.mark.parametrize('x,y,expect',[
    ([1,1,1,1],[2,3,1],[1,6,5,0]),
    ([2,3,1],[6,1,3,1],[1,1,0,0]),
    ([1,1,1,1],[6,1,3,1],[2,0,5,0]),
])
def test_sub(setup,x,y,expect):
    R7 = setup

    x = R7(x)
    y = R7(y)

    assert x-y == R7(expect)

@pytest.mark.parametrize('x,y,expect',[
    ([1,1,0],[3,2],[3,5,2,0]),
    ([1,1],[1,3,6],[1,4,2,6]),
    ([1,1,1,1],[2,3,1],[2,5,6,6,4,1]),
    ([2,3,1],[6,1,3,1],[5,6,1,5,6,1]),
    ([1,1,1,1],[6,1,3,1],[6,0,3,4,5,4,1]),
])
def test_mul(setup,x,y,expect):
    R7 = setup

    x = R7(x)
    y = R7(y)

    assert x*y == R7(expect)


@pytest.mark.parametrize('x,y,expect1,expect2',[
    ([1,1,1,1],[2,3,1],[4,5],[3,3]),
    ([2,3,1],[3,3],[3,5],[0]),
])
def test_division(setup,x,y,expect1,expect2):
    R7 = setup

    x = R7(x)
    y = R7(y)
    q,r = R7.division(x,y)

    assert q == R7(expect1)
    assert r == R7(expect2)


@pytest.mark.parametrize('x,MOD,one',[
    ([1,1,1,1],[1,0,5,4,3],[1]),
    ([2,3,1],[1,0,5,4,3],[1]),
    ([2,3,1],[1,0,5,4,3],[1]),
])
def test_ext_euclid(setup,x,MOD,one):
    R7 = setup
    
    x = R7(x)
    MOD = R7(MOD)

    # make sure is inverse
    gcd,e,_ = R7.ext_euclid(x,MOD)
    _,r = R7.division(e*x,MOD)
    assert gcd == R7(one)
    assert r == R7(one)


'''

def test_gcd(setup):
    R7 = setup

    # make sure gcd poly
    gcd,q,r = R7.ext_euclid(x,y)
    assert gcd == R7([1,1])

    # make sure inverse
    gcd,a,_ = R7.ext_euclid(x,MOD)
    assert a == R7([6,0,0,6])

'''