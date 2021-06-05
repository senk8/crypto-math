from galois_fields import GF,field_extension

def test_add():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    x = F7_4([1,1,1,1])
    y = F7_4([0,2,3,1])
    z = F7_4([6,1,3,1])

    assert x+y == F7_4([1,3,4,2])
    assert x+z == F7_4([0,2,4,2])
    assert y+z == F7_4([6,3,6,2])

def test_sub():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)


    x = F7_4([1,1,1,1])
    y = F7_4([0,2,3,1])
    z = F7_4([6,1,3,1])

    assert x-y == F7_4([1,6,5,0])
    assert x-z == F7_4([2,0,5,0])
    assert y-z == F7_4([1,1,0,0])
    assert x-x == F7_4.zero()

def test_mod():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    x = F7_4([1,1,1,1])
    y = F7_4([0,2,3,1])

    assert x%y == F7_4([0,0,3,3]) 
    assert x//y == F7_4([0,0,4,5]) 

def test_mul():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    a = F7_4([0,1,1,0])
    b = F7_4([0,0,3,2])
    except1 = F7_4([3,5,2,0])

    assert a*b == except1

    a = F7_4([0,0,1,1])
    b = F7_4([0,1,3,6])
    except1 = F7_4([1,4,2,6])

    assert a*b == except1

    x = F7_4([1,1,1,1])
    y = F7_4([0,2,3,1])
    z = F7_4([6,1,3,1])

    assert x*y == F7_4([3,1,6,0])
    assert x*z == F7_4([1,3,0,5])
    assert y*z == F7_4([4,4,2,4])
    assert (x*F7_4.zero()).is_zero()


def test_inverse():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)
    f = lambda x,y:x.inverse()*y

    x = F7_4([1,1,1,1])
    y = F7_4([6,0,0,6])
    z = F7_4([0,2,3,1])

    assert (x*y).is_one()
    assert f(x,x).is_one()
    assert f(z,z).is_one()


