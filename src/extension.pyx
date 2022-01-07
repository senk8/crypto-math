import itertools
import numpy as np


def field_extension(Fp, ord: int):
    cdef:
        int order
        int cardinality
        int p
        list v

    PR = poly_ring(Fp)
    MOD = (1, 0, 5, 4, 3)
    # MOD = (1,0,0,1,0,1)
    # MOD:Tuple[int] =MODS[ord]

    class ExField(PR):
        # ord is equal to len(MOD)-1
        order = ord
        cardinality = Fp.degree ** order
        p = Fp.degree
        v = np.array([p ** i for i in range(ord - 1, -1, -1)])

        def __init__(self, coeffs):
            super().__init__(coeffs)

        def __mul__(self, other):
            cdef list new_coeffs
            new_coeffs = mul_helper(self.coeffs, other.coeffs)
            _, r = PR.division(PR(new_coeffs), PR(MOD))
            return ExField(r.coeffs)

        def __truediv__(self, other):
            return self * other.inverse()

        def inverse(self):
            gcd, e, _ = PR.ext_euclid(self, ExField(MOD))
            if not gcd.is_one():
                return ExField.zero()
            else:
                return e

        def encode(self):
            return np.dot(self.v[: self.degree + 1], self.coeffs)

        @classmethod
        def enumerate(cls):
            return itertools.product(range(cls.p), repeat=cls.order)

        @classmethod
        def generator(cls):
            cdef int i
            import itertools

            l = [0, 1]
            coeff_pattern = itertools.product(l, repeat=5)
            for g in coeff_pattern:
                g_ = cls(g)
                # MOD-1まで1にならなければ
                for i in range(1, p ** ord - 1):
                    print(p ** ord - 1)
                    if g_ ** i == cls.one():
                        break
                    if i == MOD - 2:
                        return g_

    return ExField
