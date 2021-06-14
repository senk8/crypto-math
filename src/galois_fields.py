from __future__ import annotations
import math_util as mu
import poly_ring as pr
from functools import lru_cache
import fft

MODS = [(1),(1),(1,1,1),(1,0,1,1),(1,0,0,1,1),(1,0,0,1,0,1),(1,0,1,1,0,1,1),(1,0,0,0,0,0,1,1),(1,0,0,0,1,1,1,0,1)]

def GF(MOD):

    # closure
    class Fp(int):
        cardinality = MOD
        degree = MOD

        def __new__(self,num:int)->Fp:
            return int.__new__(self,num%MOD)

        def __add__(self,other:Fp)->Fp:
            return Fp(super().__add__(other) % MOD)

        def __sub__(self,other:Fp)->Fp:
            return Fp(super().__sub__(other) % MOD)

        def __mul__(self,other:Fp)->Fp:
            return Fp(super().__mul__(other) % MOD)

        def __truediv__(self,other:Fp)->Fp:
            return Fp(super().__mul__(pow(other,MOD-2)) % MOD)

        def __pow__(self, exp):
            res=Fp(1)
            for _ in range(exp):
                res=res*self
            return res 

        def inverse(self)->Fp:
            return pow(self,MOD-2)

        @classmethod
        def zero(cls):
            return cls(0)

        @classmethod
        def one(cls):
            return cls(1)
        
        @classmethod
        def enumerate(cls):
            return range(MOD)
        
        @classmethod
        def generator(cls)->Fp:
            for g in range(1,MOD):
                g_ = cls(g)
                # MOD-1まで1にならなければ
                for i in range(1,MOD-1):
                    if g_**i == cls.one():
                        break
                    if i == MOD-2:
                        return g_
                

    return Fp


def field_extension(Fp,ord:int):
    PR = pr.poly_ring(Fp)
    MOD:int = (1,0,5,4,3)
    #MOD:Tuple[int] =MODS[ord]

    class ExField(PR):
        order = ord
        cardinality = Fp.degree**order
        def __init__(self,coeffs):
            super().__init__(coeffs)

        def __add__(self, other)->ExField:
            if self.degree < other.degree:
                filled=mu.padding(self.coeffs,other.degree,Fp)
                res = tuple([x+y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=mu.padding(other.coeffs,self.degree,Fp)
                res = tuple([x+y for (x,y) in zip(self.coeffs,filled)])
            return ExField(res[mu.find_non_zero_index(res):])

        def __sub__(self, other):
            if self.degree < other.degree:
                filled=mu.padding(self.coeffs,other.degree,Fp)
                res = tuple([x-y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=mu.padding(other.coeffs,self.degree,Fp)
                res = tuple([x-y for (x,y) in zip(self.coeffs,filled)])
            return ExField(res[mu.find_non_zero_index(res):])

        def __mul__(self, other):
            '''
            new_coeffs = tuple(reversed(fft.fast_fourier_transform(tuple(reversed(self.coeffs)),tuple(reversed(other.coeffs)))))
            _,r = PR.division(PR(tuple(new_coeffs)),PR(MOD))
            return ExField(r.coeffs)
            '''

            d = self.degree+other.degree

            new_coeffs = [Fp(0)]*(d+1)

            for k in range(d+1):
                for i in range(k+1):
                    if self.degree-i < 0 or other.degree- (k - i) < 0:
                        continue
                    
                    new_coeffs[d-k] += self.coeffs[self.degree-i] * other.coeffs[other.degree-(k-i)]

            _,r = PR.division(PR(tuple(new_coeffs)),PR(MOD))
            return ExField(r.coeffs)
        
        def __truediv__(self,other)->Fp:
            return self*other.inverse()

        def inverse(self):
            gcd, e, _ = PR.ext_euclid(self,ExField(MOD))
            if not gcd.is_one():
                return ExField.zero()
            else:
                return e

        def monic(self):
            if self.is_monic():
                return self
            else :
                return self * ExField([self.coeffs[0].inverse()])

        @classmethod
        def enumerate(cls):
            import itertools
            return itertools.product(range(cls.p),repeat=cls.order)

    return ExField




if __name__ == "__main__":
    print(0)