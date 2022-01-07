from crypto_math import GF, poly_ring
import pytest
import numpy as np
import random


def r_setup(p):
    F = GF(p)
    R = poly_ring(F)
    return R


@pytest.mark.parametrize(
    "p,x,y,expect",
    [
        (7, [1, 1, 1, 1], [2, 3, 1], [1, 3, 4, 2]),
        (7, [2, 3, 1], [6, 1, 3, 1], [6, 3, 6, 2]),
        (7, [1, 1, 1, 1], [6, 1, 3, 1], [2, 4, 2]),
    ],
)
def test_add(p, x, y, expect):
    R = r_setup(p)

    x = R(x)
    y = R(y)

    assert x + y == R(expect)


@pytest.mark.parametrize(
    "p,x,y,expect",
    [
        (7, [1, 1, 1, 1], [2, 3, 1], [1, 6, 5, 0]),
        (7, [2, 3, 1], [6, 1, 3, 1], [1, 1, 0, 0]),
        (7, [1, 1, 1, 1], [6, 1, 3, 1], [2, 0, 5, 0]),
    ],
)
def test_sub(p, x, y, expect):
    R = r_setup(p)

    x = R(x)
    y = R(y)

    assert x - y == R(expect)


@pytest.mark.parametrize(
    "p,x,y,expect",
    [
        (7, [1, 1, 0], [3, 2], [3, 5, 2, 0]),
        (7, [1, 1], [1, 3, 6], [1, 4, 2, 6]),
        (7, [1, 1, 1, 1], [2, 3, 1], [2, 5, 6, 6, 4, 1]),
        (7, [2, 3, 1], [6, 1, 3, 1], [5, 6, 1, 5, 6, 1]),
        (7, [1, 1, 1, 1], [6, 1, 3, 1], [6, 0, 3, 4, 5, 4, 1]),
    ],
)
def test_mul(p, x, y, expect):
    R = r_setup(p)

    x = R(x)
    y = R(y)

    assert x * y == R(expect)


@pytest.mark.parametrize(
    "p,x,y,expect1,expect2",
    [
        (7, [1, 1, 1, 1], [2, 3, 1], [4, 5], [3, 3]),
        (7, [2, 3, 1], [3, 3], [3, 5], [0]),
    ],
)
def test_division(p, x, y, expect1, expect2):
    R = r_setup(p)

    x = R(x)
    y = R(y)
    q, r = R.division(x, y)

    assert q == R(expect1)
    assert r == R(expect2)

@pytest.mark.parametrize(
    "p,x,exp,expect",
    [
        (7, [1], 5, [1]),
        (7, [1, 5], 2, [1, 3, 4]),
        (7, [2, 5], 4, [2, 6, 5, 6, 2]),
        (7, [1, 5], 5, [1, 4, 5, 4, 3, 3]),
        (7, [1, 0], 5, [1, 0, 0, 0, 0, 0]),
        (7, [3, 2, 1], 5, [5, 5, 1, 1, 1, 2, 5, 4, 6, 3, 1]),
        (7, [1, 5, 4], 3, [1, 1, 3, 0, 5, 2, 1])
    ],
)
def test_pow(p, x, exp, expect):
    R = r_setup(p)
    x = R(x)
    actual = x ** exp

    # make sure is inverse
    assert actual == R(expect)


@pytest.mark.parametrize(
    "p,x,MOD,one",
    [
        (7, [1, 1, 1, 1], [1, 0, 5, 4, 3], [1]),
        (7, [2, 3, 1], [1, 0, 5, 4, 3], [1]),
        (7, [2, 3, 1], [1, 0, 5, 4, 3], [1]),
    ],
)
def test_ext_euclid(p, x, MOD, one):
    R = r_setup(p)

    x = R(x)
    MOD = R(MOD)

    # make sure is inverse
    gcd, e, _ = R.ext_euclid(x, MOD)
    _, r = R.division(e * x, MOD)
    assert gcd == R(one)
    assert r == R(one)
