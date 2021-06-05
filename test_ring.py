from galois_fields import GF
from poly_ring import poly_ring

def test_add():
    F7 = GF(7)
    R7 = poly_ring(F7)

    x = R7([1,1,1,1])
    y = R7([2,3,1])
    z = R7([6,1,3,1])

    assert x+y == R7([1,3,4,2])
    assert x+z == R7([2,4,2])
    assert y+z == R7([6,3,6,2])

def test_sub():
    F7 = GF(7)
    R7 = poly_ring(F7)

    x = R7([1,1,1,1])
    y = R7([2,3,1])
    z = R7([6,1,3,1])

    assert x-y == R7([1,6,5,0])
    assert x-z == R7([2,0,5,0])
    assert y-z == R7([1,1,0,0])

def test_mul():
    F7 = GF(7)
    R7 = poly_ring(F7)

    a = R7([1,1,0])
    b = R7([3,2])

    print(a*b)

    assert a*b == R7([3,5,2,0])

    a = R7([1,1])
    b = R7([1,3,6])

    assert a*b == R7([1,4,2,6])

    x = R7([1,1,1,1])
    y = R7([2,3,1])
    z = R7([6,1,3,1])

    assert x-y == R7([1,6,5,0])
    assert x-z == R7([2,0,5,0])
    assert y-z == R7([1,1,0,0])

def test_division():
    F7 = GF(7)
    R7 = poly_ring(F7)

    x = R7([1,1,1,1])
    y = R7([2,3,1])

    q,r = R7.division(x,y)

    assert q == R7([4,5])
    assert r == R7([3,3])

    q,r = R7.division(y,r)

    assert q == R7([3,5])
    assert r == R7.zero()


def test_ext_euclid():
    F7 = GF(7)
    R7 = poly_ring(F7)

    x = R7([1,1,1,1])
    y = R7([2,3,1])
    z = R7([6,1,3,1])
    MOD = R7([1,0,5,4,3])

    gcd,q,r = R7.ext_euclid(x,y)
    assert gcd == R7([1,1])

    # make sure inverse
    gcd,a,_ = R7.ext_euclid(x,MOD)
    assert a == R7([6,0,0,6])

    # make sure is inverse
    gcd,e,_ = R7.ext_euclid(x,MOD)
    assert gcd == R7([1])
    _,r = R7.division(e*x,MOD)
    assert r == R7([1])

    gcd,e,_ = R7.ext_euclid(y,MOD)
    assert gcd == R7([1])
    _,r = R7.division(e*y,MOD)
    assert r == R7([1])

    gcd,e,_ = R7.ext_euclid(z,MOD)
    assert gcd == R7([1])
    _,r = R7.division(e*z,MOD)
    assert r == R7([1])




