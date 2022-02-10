from gmpy2 cimport *
from gmpy2 import mpz

cdef extern from "gmp.h":
    void mpz_init(mpz_t)  
    void mpz_init_set_ui (mpz_t rop, unsigned long int op)
    void mpz_set (mpz_t rop, mpz_t op)
    char * mpz_get_str (char *str, int base, mpz_t op)
    unsigned long int mpz_get_ui (mpz_t op)
    void mpz_add (mpz_t rop, mpz_t op1, mpz_t op2)
    void mpz_sub (mpz_t rop, mpz_t op1, mpz_t op2)
    void mpz_mul (mpz_t rop, mpz_t op1, mpz_t op2)
    void mpz_powm (mpz_t rop, mpz_t base, mpz_t exp, mpz_t mod)
    void mpz_tdiv_q (mpz_t q, mpz_t n, mpz_t d)
    void mpz_mod (mpz_t r, mpz_t n, mpz_t d)
    int mpz_invert (mpz_t rop, mpz_t op1, mpz_t op2)

import_gmpy2()   # needed to initialize the C-API

def gmp_add(x,y):
    cdef mpz z = GMPy_MPZ_New(NULL)

    x = mpz(x)
    y = mpz(y)
    mpz_add(MPZ(z), MPZ(x), MPZ(y))

    return int(z)

def gmp_sub(x,y):
    cdef mpz z = GMPy_MPZ_New(NULL)

    x = mpz(x)
    y = mpz(y)
    mpz_sub(MPZ(z), MPZ(x), MPZ(y))

    return int(z)

def gmp_mul(x,y):
    cdef mpz z = GMPy_MPZ_New(NULL)

    x = mpz(x)
    y = mpz(y)
    mpz_mul(MPZ(z), MPZ(x), MPZ(y))

    return int(z)

def gmp_tdiv_q(x,y):
    cdef mpz z = GMPy_MPZ_New(NULL)

    x = mpz(x)
    y = mpz(y)
    mpz_tdiv_q(MPZ(z), MPZ(x), MPZ(y))

    return int(z)

def gmp_mod(x,y):
    cdef mpz z = GMPy_MPZ_New(NULL)

    x = mpz(x)
    y = mpz(y)
    mpz_mod(MPZ(z), MPZ(x), MPZ(y))

    return int(z)

def gmp_pow(g, e, MOD):
    cdef:
        mpz z = GMPy_MPZ_New(NULL)
        cdef mpz g_, z_, MOD_

    g_ = mpz(g)
    e_ = mpz(e)
    MOD_ = mpz(MOD)
    mpz_powm(MPZ(z), MPZ(g_), MPZ(e_), MPZ(MOD_))

    return int(z)

def gmp_invert(x, MOD):
    cdef mpz z = GMPy_MPZ_New(NULL)

    x = mpz(x)
    MOD = mpz(MOD)
    ok = mpz_invert(MPZ(z), MPZ(x), MPZ(MOD))

    if ok == 0 :
        exit(ok)

    return int(z)

