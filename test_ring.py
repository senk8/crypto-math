from src.galois_fields import GF
from src.poly_ring import poly_ring

def test_add():
    F7 = GF(7)
    R7 = poly_ring(F7)

    x = R7([1,1,1,1])
    y = R7([2,3,1])
    z = R7([6,1,3,1])

    print(x+y)
    assert x+y == R7([1,3,4,2])
    assert x+z == R7([2,4,2])
    assert y+z == R7([6,3,6,2])

def test_sub():
    F7 = GF(7)
    R7 = poly_ring(F7)

    x = R7([1,1,1,1])
    y = R7([0,2,3,1])
    z = R7([6,1,3,1])

    print(x-y)
    assert x-y == R7([1,6,5,0])
    assert x-z == R7([2,0,5,0])
    assert y-z == R7([1,1,0,0])
