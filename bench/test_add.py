import galois_fields as gf
from util import time_measurement


@time_measurement
def test_add():
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1,2])
    y = F7_4([2,4])
    for _ in range(10**6):
        z = x + y
    return

@time_measurement
def test_sub():
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1,2])
    y = F7_4([2,4])
    for _ in range(10**6):
        z = x - y
    return

@time_measurement
def test_mul():
    F7 = gf.GF(7)
    F7_4 = gf.field_extension(F7,4)
    x = F7_4([1,2])
    y = F7_4([2,4])
    for _ in range(10**6):
        z = x * y
    return



if __name__ == "__main__":
    test_mul()
