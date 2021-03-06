import itertools
from libcpp.vector cimport vector

def poly_ring(Fp):
    cdef int p
    class PolyRing:
        p = Fp.degree

        def __init__(self, coeffs):
            self.coeffs = preprocess(coeffs, Fp)
            self.degree = len(self.coeffs) - 1

        def __add__(self, other):
            cdef tuple res,filled
            if self.degree < other.degree:
                filled = padding(self.coeffs, other.degree, Fp)
                res = tuple([x + y for (x, y) in zip(filled, other.coeffs)])
            else:
                filled = padding(other.coeffs, self.degree, Fp)
                res = tuple([x + y for (x, y) in zip(self.coeffs, filled)])
            return self.__class__(res)

        def __sub__(self, other):
            cdef tuple res,filled
            if self.degree < other.degree:
                filled = padding(self.coeffs, other.degree, Fp)
                res = tuple([x - y for (x, y) in zip(filled, other.coeffs)])
            else:
                filled = padding(other.coeffs, self.degree, Fp)
                res = tuple([x - y for (x, y) in zip(self.coeffs, filled)])
            return self.__class__(res)

        def __mul__(self, other):
            cdef list new_coeffs
            new_coeffs = mul_helper(self.coeffs, other.coeffs)
            return PolyRing(new_coeffs)

        def __eq__(self, other):
            if self.degree != other.degree:
                return False
            else:
                return all([x == y for x, y in zip(self.coeffs, other.coeffs)])

        def __neq__(self, other):
            return not (self == other)

        def __str__(self):
            s = ""
            for d, x in enumerate(reversed(self.coeffs)):
                if x == 0:
                    if self.degree == 0:
                        s += str(x)
                        break
                    else:
                        continue

                if d != 0:
                    s = f"+{x}x^{d}" + s
                else:
                    s = "+" + str(x) + s

            return s.lstrip("+")

        def __pow__(self, exp):
            res = self.one()
            while exp:
                if exp & 1:
                    res *= self
                exp >>= 1
                self *= self
            return res

        def monic(self):
            if self.is_monic():
                return self
            else:
                return self * self.__class__([self.coeffs[0].inverse()])

        def is_monic(self):
            return self.coeffs[0] == 1

        def is_zero(self):
            return self == self.zero()

        def is_one(self):
            return self == self.one()

        @classmethod
        def zero(cls):
            return cls((0,))

        @classmethod
        def one(cls):
            return cls((1,))

        @classmethod
        def division(cls, lhs, rhs):
            if lhs.degree < rhs.degree:
                return cls.zero(), lhs

            quotient = cls.zero()
            reminder = lhs

            while rhs.degree <= reminder.degree and not reminder.is_zero():
                divisor = reminder.coeffs[0] / rhs.coeffs[0]
                padding = (Fp(0),) * (reminder.degree - rhs.degree)
                shifted = cls(rhs.coeffs + padding)
                temp = cls([divisor * x for x in shifted.coeffs])
                quotient += cls((divisor,) + padding)

                reminder = reminder - temp

            return quotient, reminder

        @classmethod
        def ext_euclid(cls, a, b):
            if a.is_zero():
                raise ValueError("Argument 1 is zero!")
            x = cls.one()
            y = cls.zero()
            nx = cls.zero()
            ny = cls.one()

            while not b.is_zero():
                q, r = PolyRing.division(a, b)

                tmpx = x - q * nx
                tmpy = y - q * ny

                a, b = b, r
                x, y = nx, ny
                nx, ny = tmpx, tmpy

            d = PolyRing([a.coeffs[0].inverse()])
            return d * a, d * x, d * y

    return PolyRing


cdef inline tuple preprocess(coeffs,Fp):
    cdef tuple new_coeffs
    cdef int start
    new_coeffs = tuple([ Fp(x) for x in coeffs])
    start = find_non_zero_index(new_coeffs)
    return new_coeffs[start:]
