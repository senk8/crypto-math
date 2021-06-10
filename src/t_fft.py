import math_util as mu
import cmath

def t_discrete_fourier_transform(poly,n):
    unity = get_unity(n)
    new_poly = [f(poly,unity**i,n) for i in range(n)]
    return new_poly

def t_inverse_discrete_fourier_transform(poly,n):
    unity = get_unity(n)**(-1)
    new_poly = [1/n*f(poly,unity**i,n) for i in range(n)]
    return new_poly

def f(poly,x,n):
    return sum([ c*x**i for i,c in zip(range(n),poly)])

def get_unity(n)->complex:
    unity:complex = complex(cmath.cos(2*cmath.pi/n),cmath.sin(2*cmath.pi/n))
    return unity 

def padding(poly,m,Fp=int):
    deg = len(poly)-1
    if deg < m:
        return (m-deg) * (Fp(0),) + poly
    else :
        return poly

def fast_fourier_transform(g,h):
    dg=len(g)-1
    dh=len(h)-1

    # It is required n poly to restore n-1 poly
    n = mu.pow_2_at_least(dg+dh+1)

    # n-1 poly
    m = n - 1

    g_ = discrete_fourier_transform(padding(g,m),n)
    h_ = discrete_fourier_transform(padding(h,m),n)
    f_ = tuple([ g_[i]*h_[i] for i in range(n-1,-1,-1) ])
    res = inverse_discrete_fourier_transform(f_,n)

    # epilogue
    formarize_and_rouded = tuple([ round((i*1/n).real) for i in res[n-(dg+dh+1):]])

    return formarize_and_rouded

def discrete_fourier_transform(poly, n):
    if n==1:
        assert len(poly)==1
        # The root of n to the power of 1 is 1, so
        return poly
    
    # f0 and f1 are coeffs
    f0 = [ poly[2*i+0] for i in range(n//2-1,-1,-1)]
    f1 = [ poly[2*i+1] for i in range(n//2-1,-1,-1)]

    # f0 and f1 are evaluated polynomial
    f0 = discrete_fourier_transform(f0, n//2)
    f1 = discrete_fourier_transform(f1, n//2)

    unity = get_unity(n)

    # f(u)=f0(u)+uf1(u),f(u1)=f0(u1)+u1f1(u1).....
    new_poly = [ f0[i%(n//2)]+(unity**i)*f1[i%(n//2)] for i in range(n-1,-1,-1)]
    return new_poly

def inverse_discrete_fourier_transform(poly,n):
    if n==1:
        assert len(poly)==1
        return poly

    f0 = [ poly[2*i+0] for i in range(n//2-1,-1,-1)]
    f1 = [ poly[2*i+1] for i in range(n//2-1,-1,-1)]

    f0 = inverse_discrete_fourier_transform(f0, n//2)
    f1 = inverse_discrete_fourier_transform(f1, n//2)

    unity = get_unity(n)**(-1)
    new_poly = [ f0[i%(n//2)]+(unity**i)*f1[i%(n//2)] for i in range(n-1,-1,-1)]
    return new_poly


