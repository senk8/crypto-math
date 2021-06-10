import galois_fields as gf
import pytest

ITERATION = 10**4

def test_add(benchmark):
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1,2])
    y = F7_4([2,4])
    def f():
        _ = x + y
    benchmark(f)

def test_sub(benchmark):
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1,2])
    y = F7_4([2,4])
    def f():
        _ = x - y
    benchmark(f)

def test_mul(benchmark):
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1,2])
    y = F7_4([2,4])
    def f():
        _ = x * y
    benchmark(f)

def test_div(benchmark):
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1,2])
    y = F7_4([2,4])
    def f():
        _ = x / y
    benchmark(f)