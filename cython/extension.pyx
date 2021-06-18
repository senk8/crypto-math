import itertools

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
                filled=padding(self.coeffs,other.degree,Fp)
                res = tuple([x+y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=padding(other.coeffs,self.degree,Fp)
                res = tuple([x+y for (x,y) in zip(self.coeffs,filled)])
            return ExField(res)

        def __sub__(self, other):
            cdef tuple res
            if self.degree < other.degree:
                filled=padding(self.coeffs,other.degree,Fp)
                res = tuple([x-y for (x,y) in zip(filled,other.coeffs)])
            else :
                filled=padding(other.coeffs,self.degree,Fp)
                res = tuple([x-y for (x,y) in zip(self.coeffs,filled)])
            return ExField(res)

        def __mul__(self, other):
            cdef list new_coeffs
            new_coeffs = mul_helper(self.coeffs,other.coeffs)
            _,r = PR.division(PR(new_coeffs),PR(MOD))
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



