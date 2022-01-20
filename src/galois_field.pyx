def GF(MOD: int):
    cdef:
        int cardinality
        int degree

    class Fp(int):
        cardinality = MOD
        degree = MOD

        def __new__(self, num: int):
            r = gmp_mod(num, MOD)
            return int.__new__(self, r)

        def __add__(self, other):
            res = gmp_add(self, other)
            return Fp(res)

        def __sub__(self, other):
            res = gmp_sub(self, other)
            return Fp(res)

        def __mul__(self, other):
            res = gmp_mul(self, other)
            return Fp(res)

        def __truediv__(self, other):
            e = Fp(other).inverse()
            res = gmp_mul(self, e)
            return Fp(res)

        def __pow__(self, exp: int):
            if exp == -1:
                return self.inverse()
            res = gmp_pow(self, exp, MOD)
            return Fp(res)

        def inverse(self):
            res = gmp_invert(self, MOD)
            return Fp(res)

        @classmethod
        def enumerate(cls):
            return range(MOD)

        @classmethod
        def generator(cls):
            cdef int g,i
            for g in range(1, MOD):
                g_ = cls(g)
                for i in range(1, MOD - 1):
                    if g_ ** i == cls.one():
                        break
                    if i == MOD - 2:
                        return g_

        @classmethod
        def one(cls):
            return Fp(1)
        
        @classmethod
        def zero(cls):
            return Fp(0)

    return Fp
