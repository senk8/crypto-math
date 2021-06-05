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
        def deg(self)->int:
            return MOD

    return Fp


def field_extension(Fp,order:int):
    PR = pr.poly_ring(Fp)
    MOD:int = (1,0,5,4,3)

    class ExField:
        def __init__(self,coeffs):
            start:int = mu.find_non_zero_index(coeffs)
            self.degree:int = len(coeffs[start:])-1
            self.coeffs:tuple[Fp] = tuple(map(Fp,coeffs[start:]))

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

            coeffs1 = tuple(reversed(self.coeffs))
            coeffs2 = tuple(reversed(other.coeffs))

            for k in range(d+1):
                for i in range(k+1):
                    if len(coeffs1) <= i or len(coeffs2) <= k - i:
                        continue

                    new_coeffs[k] += coeffs1[i] * coeffs2[k-i]

            _,r = PR.division(PR(tuple(reversed(new_coeffs))),PR(MOD))
            return ExField(r.coeffs)

        def __eq__(self, other):
            if self.degree != other.degree:
                return False
            else:
                return all([ x==y for x ,y in zip(self.coeffs,other.coeffs)])
        
        def __neq__(self, other):
            return not (self == other)

        def __str__(self):
            s = ""
            for d,x in enumerate(reversed(self.coeffs)):
                if x == 0 :
                    if self.degree==0:
                        s+=str(x)
                        break
                    else:
                        continue

                if d != 0:
                    s = f"+{x}x^{d}" + s
                else:
                    s = "+" + str(x) + s

            return s.lstrip("+")

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

        def is_monic(self):
            return self.coeffs[0]==1
        
        def is_zero(self):
            return self == ExField.zero()

        def is_one(self):
            return self == ExField.one()
        
        @classmethod
        def zero(cls):
            return cls((0,))

        @classmethod
        def one(cls):
            return cls((1,))

        
    return ExField




if __name__ == "__main__":
    print(0)