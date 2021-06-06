from galois_fields import GF,field_extension

def test_add():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    x = F7_4([1,1,1,1])
    y = F7_4([2,3,1])
    z = F7_4([6,1,3,1])

    assert x+y == F7_4([1,3,4,2])
    assert y+z == F7_4([6,3,6,2])
    assert x+z == F7_4([2,4,2])

def test_sub():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    x = F7_4([1,1,1,1])
    y = F7_4([2,3,1])
    z = F7_4([6,1,3,1])

    assert x-y == F7_4([1,6,5,0])
    assert y-z == F7_4([1,1,0,0])
    assert x-z == F7_4([2,0,5,0])

    assert x-x == F7_4.zero()

def test_mul():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    a = F7_4([1,1,0])
    b = F7_4([3,2])
    except1 = F7_4([3,5,2,0])

    assert a*b == except1

    a = F7_4([1,1])
    b = F7_4([1,3,6])
    except1 = F7_4([1,4,2,6])

    assert a*b == except1

    x = F7_4([1,1,1,1])
    y = F7_4([2,3,1])
    z = F7_4([6,1,3,1])

    assert x*y == F7_4([3,1,6,0])
    assert y*z == F7_4([4,4,2,4])
    assert x*z == F7_4([1,3,0,5])

    assert (x*F7_4.zero()).is_zero()

def test_div():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    x = F7_4([1,1,1,1])
    y = F7_4([2,3,1])
    z = F7_4([6,1,3,1])

    assert x/y == F7_4([2,6,4,6])
    assert y/z == F7_4([0,6,5,4])
    assert x/z == F7_4([2,5,1,5])


def test_inverse():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)
    f = lambda x,y:x.inverse()*y

    x = F7_4([1,1,1,1])
    y = F7_4([6,0,0,6])
    z = F7_4([2,3,1])

    assert (x*y).is_one()
    assert (x*x.inverse()).is_one()
    assert (z*z.inverse()).is_one()

def test_pow():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)

    x = F7_4([1,1,1,1])
    y = F7_4([6,0,0,6])
    z = F7_4([2,3,1])

    print(x**2)
    print(x*x)
    assert x**2 == x*x
    assert x**3 == x*x*x


