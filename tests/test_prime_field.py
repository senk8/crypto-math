import crypto_math as gf
import pytest
import random

#p = gf.get_prime()

ITERATION = 10 ** 3

def g_setup(p):
    F = gf.GF(p)
    return F


@pytest.mark.parametrize(
    "p",
    [
        (2),
        (3),
        (5),
        (7),
        (11),
        (101),
        (65537),
    ],
)
def test_add_ramdom(p):
    F = g_setup(p)

    for _ in range(ITERATION):
        
        x = random.randint(0, p)
        y = random.randint(0, p)

        actual = F(x)+F(y)
        expect = (x + y) % p

        assert actual == expect

@pytest.mark.parametrize(
    "p",
    [
        (2),
        (3),
        (5),
        (7),
        (11),
        (101),
        (65537),
    ],
)
def test_sub_ramdom(p):
    F = g_setup(p)

    for _ in range(ITERATION):
        
        x = random.randint(0, p)
        y = random.randint(0, p)

        actual = F(x) * F(y)
        expect = (x * y) % p

        assert actual == expect

@pytest.mark.parametrize(
    "p",
    [
        (2),
        (3),
        (5),
        (7),
        (11),
        (101),
        (65537),
    ],
)
def test_mul_ramdom(p):
    F = g_setup(p)

    for _ in range(ITERATION):
        
        x = random.randint(0, p)
        y = random.randint(0, p)

        actual = F(x) * F(y)
        expect = (x * y) % p

        assert actual == expect

@pytest.mark.parametrize(
    "p",
    [
        (2),
        (3),
        (5),
        (7),
        (11),
        (101),
        (65537),
    ],
)
def test_div_ramdom(p):
    F = g_setup(p)

    for _ in range(ITERATION):
        
        x = random.randint(1, p)
        y = random.randint(1, p)

        if x % p == 0 or y % p == 0:
            continue

        actual = F(x) // F(y)
        expect = (x // y) % p

        assert actual == expect

@pytest.mark.parametrize(
    "p",
    [
        (2),
        (3),
        (5),
        (7),
        (11),
        (101),
        (65537),
    ],
)
def test_pow_ramdom(p):
    F = g_setup(p)

    for _ in range(ITERATION):
        
        x = random.randint(1, p)
        y = random.randint(1, p)

        actual = F(x) ** y
        expect = (x ** y) % p

        print(f"{x} ** {y}")
        assert actual == expect
    

@pytest.mark.parametrize(
    "p",
    [
        (2),
        (3),
        (5),
        (7),
        (11),
        (101),
        (65537),
    ],
)
def test_inverse_ramdom(p):
    F = g_setup(p)

    for _ in range(ITERATION):
        x = random.randint(1, p)

        if x % p == 0:
            continue

        actual = F(x).inverse()
        expect = pow(x, -1,  p)

        print(f"{x} ^ -1")
        assert actual == expect