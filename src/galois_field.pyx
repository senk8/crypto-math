from gmpy2 cimport *
from gmpy2 import mpz

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
        def init_windowing(self, g, int h, int l):
            """
                m = range of value. For example, you would like to include 1024bit number, then you specify m = 2**1024;
            """
            cdef: 
                int b = h
                int i 
                mpz_t[1024] gs 
                mpz mod = mpz(MOD)
                mpz base = mpz(g)
                mpz b_ = mpz(b)

            if 2 > b:
                raise ValueError('b is lower than 2')

            init_gs(gs, base, b_, mod, l)

            def f(exp):
                cdef:
                    int j, i, e
                    vector[int] es = encode_bit_list(mpz(exp), b, l)
                    mpz res = GMPy_MPZ_New(NULL)

                helper_windowing(res, h, mod, es, gs)
                return int(res)

            return f

        def power(self, n):
            cdef:
                mpz x_ = mpz(1)
                mpz a_ = mpz(self)
                mpz n_ = mpz(n)
                mpz mod = mpz(MOD)

            while n_:
                if n_ & 1:
                    mpz_mul(MPZ(x_) , MPZ(x_) , MPZ(a_))
                    mpz_mod(MPZ(x_) , MPZ(x_) , MPZ(mod))
                n_ >>= 1
                mpz_mul(MPZ(a_) , MPZ(a_) , MPZ(a_))
                mpz_mod(MPZ(a_) , MPZ(a_), MPZ(mod))

            return int(x_)


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


cdef inline vector[int] encode_bit_list(mpz n, int base, int l):
    cdef: 
        int i
        vector[int] res

    res.resize(l)
    for i in range(0,l):
        res[i] = n%base
        n //= base
        if 0 >= n:
            break 

    return res

cdef inline void init_gs(mpz_t[1024] gs, mpz base, mpz exp, mpz mod, int l):
    for i in range(0, l):
        mpz_init(gs[i])
        mpz_powm(gs[i], MPZ(base), MPZ(exp**i), MPZ(mod))

cdef inline void helper_windowing(mpz res, int h, mpz mod, vector[int] es, mpz_t[1024] gs):
    cdef:
        mpz_t A, B
        int i, e, j
        char* s = NULL

    mpz_init_set_ui(A, 1)
    mpz_init_set_ui(B, 1)

    for j in range(h-1, 0, -1):
        for i, e in enumerate(es):
            if e == j: 
                mpz_mul(B , B, gs[i])
                mpz_mod(B , B, MPZ(mod))

        mpz_mul(A, A, B)
        mpz_mod(A, A, MPZ(mod))

    mpz_set(MPZ(res), A)    