import math_util as mu
import copy as cp

def poly_ring(Fp):
    class PolyRing :
        def __init__(self,coeffs):
            start = mu.find_non_zero_index(coeffs)
            self.degree = len(coeffs[start:])-1
            self.coeffs = tuple(map(Fp,coeffs[start:]))
        
        def __add__(self, other):
            if self.degree != other.degree:
                self,other = mu.align_coeffs(Fp,self,other)

            res = tuple([x+y for (x,y) in zip(self.coeffs,other.coeffs)])
            return PolyRing(res[mu.find_non_zero_index(res):])

        def __sub__(self, other):
            if self.degree != other.degree:
                self,other = mu.align_coeffs(Fp,self,other)

            res = tuple([x-y for (x,y) in zip(self.coeffs,other.coeffs)])
            return PolyRing(res[mu.find_non_zero_index(res):])

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

            return PolyRing(tuple(reversed(new_coeffs)))
        
        def __eq__(self, other):
            if self.degree != other.degree:
                return False
            else:
                return all([ x==y for x ,y in zip(self.coeffs,other.coeffs)])
        
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

        def monic(self):
            if self.is_monic():
                return self
            else :
                return self * PolyRing([self.coeffs[0].inverse()])

        def is_monic(self):
            return self.coeffs[0]==1
        
        def is_zero(self):
            return self == PolyRing.zero()

        def is_one(self):
            return self == PolyRing.one()
        
        @classmethod
        def zero(cls):
            return cls((0,))

        @classmethod
        def one(cls):
            return cls((1,))

        @classmethod
        def division(cls,lhs,rhs):
            if lhs.degree<rhs.degree:
                return cls.zero(),lhs

            quotient = cls.zero()
            reminder = lhs

            while rhs.degree<=reminder.degree and not reminder.is_zero():
                divisor = reminder.coeffs[0] / rhs.coeffs[0]
                padding = (0,)*(reminder.degree-rhs.degree)
                shifted =  cls(rhs.coeffs+padding)
                temp = cls([ divisor*x for x in shifted.coeffs ])
                quotient += cls((divisor,)+padding)

                reminder = reminder - temp

            return quotient,reminder

        @classmethod
        def ext_euclid(cls,a,b):
            x = cls.one()
            y = cls.zero()
            nx = cls.zero()
            ny = cls.one()

            while not b.is_zero():
                q,r = PolyRing.division(a,b)

                tmpx = x - q*nx
                tmpy = y - q*ny

                a,b=b,r
                x,y=nx,ny
                nx,ny=tmpx,tmpy

            d = PolyRing([a.coeffs[0].inverse()])
            return d*a,d*x,d*y

    return PolyRing

if __name__ == "__main__":
    import galois_fields as gf
    F7 = gf.GF(7)
    R7 = poly_ring(F7)

    x = R7([1,1,1,1])
    MOD = R7([1,0,5,4,3])

    gcd,q,r = R7.ext_euclid(x,MOD)
    assert q == R7([6,0,0,6])