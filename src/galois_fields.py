from __future__ import annotations
from typing import List
import math_util as mu
import poly_ring as pr

def GF(MOD):

    # closure
    class Fp(int):
        def __new__(self,num:int)->Fp:
            return int.__new__(self,num%MOD)

        def __add__(self,other:Fp)->Fp:
            return Fp(super().__add__(other) % MOD)

        def __sub__(self,other:Fp)->Fp:
            return Fp(super().__sub__(other) % MOD)

        def __mul__(self,other:Fp)->Fp:
            return Fp(super().__mul__(other) % MOD)

        def __truediv__(self,other:Fp)->Fp:
            return Fp(super().__mul__(pow(other,MOD-2,MOD)) % MOD)

        def inverse(self)->Fp:
            return pow(self,MOD-2,MOD)

        @classmethod
        def degree(cls)->int:
            return MOD

        @classmethod
        def zero(cls):
            return cls(0)

        @classmethod
        def one(cls):
            return cls(1)
        
        @classmethod
        def enumerate(cls)->int:
            return range(MOD)

    return Fp


def field_extension(Fp,ord:int):
    PR = pr.poly_ring(Fp)
    MOD:int = (1,0,5,4,3)

    class ExField(PR):
        def __init__(self,coeffs):
            super().__init__(coeffs)

        def __add__(self, other)->ExField:
            if self.degree != other.degree:
                self,other = mu.align_coeffs(Fp,self,other)

            res:tuple = tuple([x+y for (x,y) in zip(self.coeffs,other.coeffs)])
            return ExField(res[mu.find_non_zero_index(res):])

        def __sub__(self, other):
            if self.degree != other.degree:
                self,other = mu.align_coeffs(Fp,self,other)

            res = tuple([x-y for (x,y) in zip(self.coeffs,other.coeffs)])
            return ExField(res[mu.find_non_zero_index(res):])

        def __mul__(self, other):
            d = self.degree+other.degree

            new_coeffs = [Fp(0)]*(d+1)

            for k in range(d+1):
                for i in range(k+1):
                    if self.degree-i < 0 or other.degree- (k - i) < 0:
                        continue
                    
                    new_coeffs[d-k] += self.coeffs[self.degree-i] * other.coeffs[other.degree-(k-i)]

            _,r = PR.division(PR(tuple(new_coeffs)),PR(MOD))
            return ExField(r.coeffs)

        def __pow__(self, other):
            if other == 0:
                return ExField.one()
            else:
                for i in range(other):
                    self=self*self
                return self

        def inverse(self):
            gcd, e, f = PR.ext_euclid(self,ExField(MOD))
            if not gcd.is_one():
                return ExField.zero()
            else:
                return e

        def monic(self):
            if self.is_monic():
                return self
            else :
                return self * ExField([self.coeffs[0].inverse()])

        def is_zero(self):
            return self == ExField.zero()

        def is_one(self):
            return self == ExField.one()

        @classmethod
        def enumerate(self):
            import itertools
            return itertools.product(range(Fp.degree()),repeat=ExField.order())

        @classmethod
        def cardinality(cls):
            return Fp.degree()**cls.order()

        @classmethod
        def order(cls):
            return ord
        
        
    return ExField




if __name__ == "__main__":
    print(0)