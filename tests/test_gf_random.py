from galois_fields import GF,field_extension
import pytest
import random
import numpy as np

def g_setup(p,n):
    F = GF(p)
    EF = field_extension(F,n)
    return EF

@pytest.mark.parametrize('p,n',[
    (7,4),
])  
def test_add_ramdom(p,n):
    EF = g_setup(p,n)

    for _ in range(10**2):
        n = random.randint(0,10**2)
        x = np.poly1d([ random.randint(0,10**2) for _ in range(n)])
        y = np.poly1d([ random.randint(0,10**2) for _ in range(n)])
        actual = EF(list(x.coeffs))+EF(list(y.coeffs))
        expect = EF(list((x+y).coeffs))

        assert actual == expect 

@pytest.mark.parametrize('p,n',[
    (7,4),
])  
def test_sub_random(p,n):
    EF = g_setup(p,n)

    for _ in range(10**2):
        n = random.randint(0,10**2)
        x = np.poly1d([ random.randint(0,10**2) for _ in range(n)])
        y = np.poly1d([ random.randint(0,10**2) for _ in range(n)])
        actual = EF(list(x.coeffs))-EF(list(y.coeffs))
        expect = EF(list((x-y).coeffs))

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
def test_mul_random(p,MOD):
    EF = g_setup(p,len(MOD)-1)
    
    for _ in range(10**2):
        n = random.randint(0,len(MOD)-1)
        x = np.poly1d([ random.randint(0,10) for _ in range(n)])
        y = np.poly1d([ random.randint(0,10) for _ in range(n)])
        mod = np.poly1d(MOD)
        _,expect = (x*y)/mod
        actual = EF(x.coeffs)*EF(y.coeffs)
        print(expect)
        print(actual)
        assert EF(expect.coeffs) == actual


