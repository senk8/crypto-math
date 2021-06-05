def find_non_zero_index(seq):
    for i,x in enumerate(seq):
        if x!=0:
            return i
    return len(seq)-1

def poly_ring(Fp):
    class PolyRing :
        def __init__(self,coeffs):
            self.degree = len(coeffs)-1
            self.coeffs = tuple(map(Fp,coeffs))
        
        def __add__(self, other):
            if self.degree != other.degree:
                self,other = self.align_coeffs(other)
                print(f"{self.coeffs}:{other.coeffs}")

            res = [0]*len(self.coeffs)

            for i,(x,y) in enumerate(zip(self.coeffs,other.coeffs)):
                res[i]=x+y
                
            return PolyRing(res)

        def __sub__(self, other):
            if self.degree != other.degree:
                self,other = self.align_coeffs(other)

            res = [0]*len(self.coeffs)
            for i,(x,y) in enumerate(zip(self.coeffs,other.coeffs)):
                res[i]=x-y
                
            return PolyRing(res)
        
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
        
        def align_coeffs(self,other):
            if self.degree == other.degree:
                return self,other
            elif self.degree < other.degree:
                return PolyRing((other.degree-self.degree)*(Fp(0),)+self.coeffs),other
            else:
                return self,PolyRing((self.degree-other.degree)*(Fp(0),)+other.coeffs)

    return PolyRing