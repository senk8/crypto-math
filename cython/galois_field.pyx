import math_util as mu
import itertools
from libcpp.vector cimport vector
from functools import lru_cache

def poly_ring(Fp):
    class PolyRing :
        p = Fp.degree
        def __init__(self,coeffs):
            self.coeffs,self.degree = self.preprocess(coeffs,Fp)
 
        def __add__(self, other):
            if self.degree < other.degree:
                filled=mu.padding(self.coeffs,other.degree,Fp)
                res = tuple([x+y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=mu.padding(other.coeffs,self.degree,Fp)
                res = tuple([x+y for (x,y) in zip(self.coeffs,filled)])
            return PolyRing(res)

        def __sub__(self, other):
            if self.degree < other.degree:
                filled=mu.padding(self.coeffs,other.degree,Fp)
                res = tuple([x-y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=mu.padding(other.coeffs,self.degree,Fp)
                res = tuple([x-y for (x,y) in zip(self.coeffs,filled)])
            return PolyRing(res)

        def __mul__(self, other):
            return PolyRing(self.multiply_conv(other))
       
        def multiply_conv(self,other):
            d = self.degree+other.degree

            new_coeffs = [Fp(0)]*(d+1)

            for k in range(d+1):
                for i in range(k+1):
                    if self.degree-i < 0 or other.degree- (k - i) < 0:
                        continue
                    
                    new_coeffs[d-k] += self.coeffs[self.degree-i] * other.coeffs[other.degree-(k-i)]
            
            return new_coeffs
        
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

        
        def __pow__(self, exp):
            res=self.one()
            for _ in range(exp):
                res=res*self
            return res 

        def monic(self):
            if self.is_monic():
                return self
            else :
                return self * PolyRing([self.coeffs[0].inverse()])

        def is_monic(self):
            return self.coeffs[0]==1
        
        def is_zero(self):
            return self == self.zero()

        def is_one(self):
            return self == self.one()

        def preprocess(self,coeffs,Fp):
            new_coeffs = tuple([ Fp(x) for x in coeffs])
            start = mu.find_non_zero_index(new_coeffs)
            return new_coeffs[start:],len(new_coeffs[start:])-1

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
                padding = (Fp(0),)*(reminder.degree-rhs.degree)
                shifted =  cls(rhs.coeffs+padding)
                temp = cls([ divisor*x for x in shifted.coeffs ])
                quotient += cls((divisor,)+padding)

                reminder = reminder - temp

            return quotient,reminder

        @classmethod
        def ext_euclid(cls,a,b):
            if a.is_zero():
                raise ValueError("Argument 1 is zero!")
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


def GF(MOD:int):
    cdef:
        int cardinality
        int degree

    # closure
    class Fp(int):
        cardinality = MOD
        degree = MOD

        def __new__(self,num:int):
            return int.__new__(self,num%MOD)

        def __add__(self,other):
            return Fp(super().__add__(other) % MOD)

        def __sub__(self,other):
            return Fp(super().__sub__(other) % MOD)

        def __mul__(self,other):
            return Fp(super().__mul__(other) % MOD)

        def __truediv__(self,other):
            return Fp(super().__mul__(pow(other,MOD-2)) % MOD)

        def __pow__(self, exp:int):
            cdef int g = int(self)
            return Fp(g**exp)

        def inverse(self):
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
        def generator(cls):
            cdef int g,i
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
    cdef:
        int order
        int cardinality
        int p

    PR = poly_ring(Fp)
    MOD = (1,0,5,4,3)
    #MOD:Tuple[int] =MODS[ord]

    class ExField(PR):
        order = ord
        cardinality = Fp.degree**order
        p = Fp.degree
        def __init__(self,coeffs):
            super().__init__(coeffs)

        def __add__(self, other):
            cdef tuple res
            if self.degree < other.degree:
                filled=mu.padding(self.coeffs,other.degree,Fp)
                res = tuple([x+y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=mu.padding(other.coeffs,self.degree,Fp)
                res = tuple([x+y for (x,y) in zip(self.coeffs,filled)])
            return ExField(res[mu.find_non_zero_index(res):])

        def __sub__(self, other):
            cdef tuple res
            if self.degree < other.degree:
                filled=mu.padding(self.coeffs,other.degree,Fp)
                res = tuple([x-y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=mu.padding(other.coeffs,self.degree,Fp)
                res = tuple([x-y for (x,y) in zip(self.coeffs,filled)])
            return ExField(res[mu.find_non_zero_index(res):])

        def __mul__(self, other):
            cdef int d,i,k
            cdef list new_coeffs

            d = self.degree+other.degree

            '''

            new_coeffs = [0]*(d+1)

            for k in range(d+1):
                for i in range(k+1):
                    if self.degree-i < 0 or other.degree- (k - i) < 0:
                        continue
                    
                    new_coeffs[d-k] += self.coeffs[self.degree-i] * other.coeffs[other.degree-(k-i)]
            '''

            new_coeffs = mul_helper(d,self.coeffs,other.coeffs)
            _,r = PR.division(PR(tuple(new_coeffs)),PR(MOD))
            return ExField(r.coeffs)
        
        def __truediv__(self,other):
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
            return itertools.product(range(cls.p),repeat=cls.order)

    return ExField



cdef vector[int] mul_helper(d:int,lhs:tuple,rhs:tuple):
    cdef:
        int k
        int i
        vector[int] new_coeffs
        int ld = len(lhs) - 1
        int rd = len(rhs) - 1
    
    new_coeffs.resize(d)
    
    for k in range(d+1):
        for i in range(k+1):
            if ld-i < 0 or rd- (k - i) < 0:
                continue
                    
            new_coeffs[d-k] += lhs[ld-i] * rhs[rd-(k-i)]
     
    return new_coeffs


def test1():
    cdef list x
    x = helper()
    return x

cdef vector[int] helper():
    cdef:
        int i = 0
        int n  = 1000000
        vector[int] res
    res.resize(n)
    for i in range(n):
        res[i]=i
    return res

def test2():
    cdef int i
    cdef int n = 1000000
    return [ i for i in range(n)]

cpdef test3():
    cdef int i
    cdef int n = 1000000
    return [ i for i in range(n)]

cpdef test4():
    return helper4()

cdef list helper4():
    cdef int i
    cdef int n = 1000000
    return [ i for i in range(n)]
