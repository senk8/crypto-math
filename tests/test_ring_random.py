from galois_fields import GF
from poly_ring import poly_ring
import pytest
import numpy as np
import random

def r_setup(p):
    F = GF(p)
    R = poly_ring(F)
    return R

@pytest.mark.parametrize('p',[
    2,
    3,
    5,
    7,
    11,
    101,
    257,
    65537,
])  
def test_add_random(p):
    R = r_setup(p)

    for _ in range(10**2):
        x = np.poly1d([ random.randint(0,10**2) for _ in range(random.randint(1,10**2))])
        y = np.poly1d([ random.randint(0,10**2) for _ in range(random.randint(1,10**2))])
        actual = R(x.coeffs)+R(y.coeffs)
        expect = R((x+y).coeffs)

        assert actual == expect 

@pytest.mark.parametrize('p',[
    2,
    3,
    5,
    7,
    11,
    101,
    257,
    65537,
])  
def test_sub_random(p):
    R = r_setup(p)

    for _ in range(10**2):
        x = np.poly1d([ random.randint(0,10**2) for _ in range(random.randint(1,10**2))])
        y = np.poly1d([ random.randint(0,10**2) for _ in range(random.randint(1,10**2))])
        actual = R(x.coeffs)-R(y.coeffs)
        expect = R((x-y).coeffs)

        assert actual == expect 


@pytest.mark.parametrize('p',[
    2,
    3,
    5,
    7,
    11,
    101,
    257,
    65537,
])  
def test_mul_random(p):
    R = r_setup(p)

    for _ in range(10**2):
        x = np.poly1d([ random.randint(0,10**2) for _ in range(random.randint(1,10**2))])
        y = np.poly1d([ random.randint(0,10**2) for _ in range(random.randint(1,10**2))])
        actual = R(x.coeffs)*R(y.coeffs)
        expect = R((x*y).coeffs)

        assert actual == expect 

@pytest.mark.parametrize('p,MOD',[
    (2,(1,1,1)),
    (3,(1,0,2,1)),
    (5,(1,0,4,4,2)),
    (7,(1,0,0,0,1,1)),
    (11,(1,0,3,4,6,7,2)),
    (101,(1,0,0,0,0,0,6,99)),
    (65537,(1,1,3,11,44,65484,153,53377,59)),
])
def test_divison_random(p,MOD):
    R = r_setup(p)
    
    for _ in range(10**2):
        n = random.randint(1,(len(MOD)-1)*2)
        x = np.poly1d([ random.randint(0,p) for _ in range(n)])
        y = np.poly1d(MOD)
        expect_q,expect_r = x/y
        actual_q,actual_r = R.division(R(x.coeffs),R(y.coeffs))
        assert R(expect_q.coeffs) == actual_q
        assert R(expect_r.coeffs) == actual_r

@pytest.mark.parametrize('p,MOD',[
    (2,(1,1,1)),
    (3,(1,0,2,1)),
    (5,(1,0,4,4,2)),
    (7,(1,0,0,0,1,4)),
    (11,(1,0,3,4,6,7,2)),
    (101,(1,0,0,0,0,0,6,99)),
    (65537,(1,1,3,11,44,65484,153,53377,59)),
])
def test_ext_euclid_random(p,MOD):
    R = r_setup(p)
    y = R(MOD)
    for _ in range(10**2):
        n = random.randint(1,len(MOD)-1)
        x = R([random.randint(0,p) for _ in range(n)])
        if x.is_zero():
                continue
        gcd,e,_ = R.ext_euclid(x,y)
        _,r = R.division(e*x,y)
        assert gcd == R.one()
        assert r == R.one()

