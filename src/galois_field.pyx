def GF(MOD: int):
    cdef:
        int cardinality
        int degree

    class Fp(int):
        cardinality = MOD
        degree = MOD

        def __new__(self, num: int):
            return int.__new__(self, num % MOD)

        def __add__(self, other):
            return Fp(super().__add__(other) % MOD)

        def __sub__(self, other):
            return Fp(super().__sub__(other) % MOD)

        def __mul__(self, other):
            return Fp(super().__mul__(other) % MOD)

        def __truediv__(self, other):
            return Fp(super().__mul__(pow(other, MOD - 2)) % MOD)

        def __pow__(self, exp: int):
            cdef int g = int(self)
            res = pow(g,exp,MOD)
            return Fp(res)

        def inverse(self):
            return pow(self, MOD - 2)

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
