from galois_fields import GF,field_extension
import pytest

@pytest.fixture
def setup():
    F7 = GF(7)
    F7_4 = field_extension(F7,4)
    return F7_4

@pytest.mark.parametrize('x,y,expect',[
    ([1,1,1,1],[2,3,1],[1,3,4,2]),
    ([2,3,1],[6,1,3,1],[6,3,6,2]),
    ([1,1,1,1],[6,1,3,1],[2,4,2]),
])
def test_add(setup,x,y,expect):
    F7_4 = setup

    x = F7_4(x)
    y = F7_4(y)

    assert x+y == F7_4(expect)

@pytest.mark.parametrize('x,y,expect',[
    ([1,1,1,1],[2,3,1],[1,6,5,0]),
    ([2,3,1],[6,1,3,1],[1,1,0,0]),
    ([1,1,1,1],[6,1,3,1],[2,0,5,0]),
    ([1,1,1,1],[1,1,1,1],[0]),
])
def test_sub(setup,x,y,expect):
    F7_4 = setup

    x = F7_4(x)
    y = F7_4(y)

    assert x-y == F7_4(expect)

@pytest.mark.parametrize('x,y,expect',[
    ([1,1,0],[3,2],[3,5,2,0]),
    ([1,1],[1,3,6],[1,4,2,6]),
    ([1,1,1,1],[2,3,1],[3,1,6,0]),
    ([2,3,1],[6,1,3,1],[4,4,2,4]),
    ([1,1,1,1],[6,1,3,1],[1,3,0,5]),
    ([1,1,1,1],[0],[0]),
])
def test_mul(setup,x,y,expect):
    F7_4 = setup

    x = F7_4(x)
    y = F7_4(y)
    
    assert x*y == F7_4(expect)

@pytest.mark.parametrize('x,y,expect',[
    ([1,1,1,1],[2,3,1],[2,6,4,6]),
    ([2,3,1],[6,1,3,1],[0,6,5,4]),
    ([1,1,1,1],[6,1,3,1],[2,5,1,5]),
])
def test_div(setup,x,y,expect):
    F7_4 = setup

    x = F7_4(x)
    y = F7_4(y)

    assert x/y == F7_4(expect)


def test_inverse(setup):
    F7_4 = setup
    f = lambda x,y:x.inverse()*y

    x = F7_4([1,1,1,1])
    y = F7_4([6,0,0,6])
    z = F7_4([2,3,1])

    assert (x*y).is_one()
    assert (x*x.inverse()).is_one()
    assert (z*z.inverse()).is_one()

@pytest.mark.parametrize('x,e',[
    ([1,1,1,1],3),
    ([2,3,1],3),
    ([6,1,3,1],3),
    ([6,1,3,1],0),
    ([6,1,3,1],1),
])
def test_pow(setup,x,e):
    F7_4 = setup

    x = F7_4(x)
    a = F7_4.one()

    for _ in range(e):
        a*=x

    assert x**e == a


