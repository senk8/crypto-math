import crypto_math as gf
import pytest
import random, math

ITERATION = 10 ** 3

@pytest.mark.parametrize(
    "g,h,l,p",
    [
        (4, 4, 5, 17),
        (3, 4, 5, 1483),
        (3, 2, 5, 911),
        (3, 10, 5, 59),
        (3, 22, 3, 1013),
    ],
)
def test_windowing(g, h, l, p):
    R = gf.GF(p)
    f = R.init_windowing(g, h, l)
    
    for _ in range(ITERATION):
        e = random.randint(0,h**l-1)
        res = g ** e
        assert  res % p == f(e)

@pytest.mark.parametrize(
    "g,h,l,p",
    [
        (3, 16, 3, 17),
        (4, 4, 5, 17),
        (3, 4, 5, 1483),
        (3, 2, 5, 911),
        (3, 10, 5, 59),
        (3, 22, 3, 1013),
    ],
)
def test_euclidean(g, h, l, p):
    R = gf.GF(p)
    f = gf.init_euclidean(R(g), h, l)
    
    for _ in range(ITERATION):
        e = random.randint(0,h**l-1)
        res = R(g) ** e % p
        assert  res == f(e)

# hは最大値ビット数
@pytest.mark.parametrize(
    "g, l, h, v, p",
    [
        #(2960, 1024, 4, 8, 17),
        (3, 10, 3, 3, 911),
    ],
)
def test_comb(g, l, h, v, p):
    #p = 89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270413618581675255342293149119973622969239858152417678164812113740223
    #q = (p - 1)//2
    #Domain = gf.GF(q)
    #Range = gf.GF(p)
    Domain = gf.GF(p)
    g = Domain(g)

    a = int(math.ceil(l / h))
    b = int(math.ceil(a / v))

    f = gf.init_comb(g, l, h, v, a, b)

    for _ in range(ITERATION):
        e = random.randint(0, h**l-1)
        assert g ** e % p == f(e)