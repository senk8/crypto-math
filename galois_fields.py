import math_util as mu

def GF(MOD):

    # closure
    class Fp(int):
        def __new__(self,num):
            return int.__new__(self,num%MOD)

        def __add__(self,other):
            return Fp(super().__add__(other) % MOD)

        def __sub__(self,other):
            return Fp(super().__sub__(other) % MOD)

        def __mul__(self,other):
            return Fp(super().__mul__(other) % MOD)

        def __truediv__(self,other):
            return Fp(super().__mul__(pow(other,MOD-2,MOD)) % MOD)

        def inverse(self):
            return pow(self,MOD-2,MOD)

        @classmethod 
        def deg(self):
            return MOD

    return Fp

def field_extension(Fp,order):
    MOD = (Fp(1),Fp(0),Fp(5),Fp(4),Fp(3))

    class ExField:
        def __init__(self,coeffs=None):
            assert len(coeffs)==order
            max_degree = order-1

            if all([ x == 0 for x in coeffs]):
                self.degree = 0
                self.leading_index = max_degree-self.degree
                self.coeffs = tuple(map(Fp,coeffs))
            else :
                # 初めて０以外が現れるインデックス
                leading_index = mu.find_non_zero_index(coeffs)

                self.degree = len(coeffs[leading_index:])-1
                self.leading_index = max_degree-self.degree
                self.coeffs = tuple(map(Fp,coeffs))

                assert self.coeffs[leading_index]!=0


        def __add__(self, other):
            res = [0]*order

            for i,(x,y) in enumerate(zip(self.coeffs,other.coeffs)):
                res[i]=x+y
                
            return ExField(res)

        def __sub__(self, other):
            res = [0]*order

            for i,(x,y) in enumerate(zip(self.coeffs,other.coeffs)):
                res[i]=x-y
                
            return ExField(res)

        def __mul__(self, other):
            # 新しい多項式の次数
            d = self.degree+other.degree

            # 新しい多項式の次数＋１が新しい多項式の係数の数になる。（０次元も含むため）
            new_coeffs = [Fp(0)]*(d+1)

            coeffs1 = tuple(reversed(self.coeffs))
            coeffs2 = tuple(reversed(other.coeffs))

            # 0次元からd次元まで繰り返す
            for k in range(d+1):
                # 例えば、新しい多項式の3次の係数はa_3b_0+a_0b_3+a_2b_1+a_1b_2となるのでa_ib_k-iで計算する。
                for i in range(k+1):
                    # リスト外参照を回避する
                    if order <= i or order <= k - i:
                        continue

                    # 新しい多項式のk次の係数に加算する
                    new_coeffs[k] += coeffs1[i] * coeffs2[k-i]

            new_coeffs = ExField.mod(tuple(reversed(new_coeffs)),MOD)
            return ExField(new_coeffs)

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

        def monic(self):
            if self.is_monic():
                return self
            else :
                e = self.coeffs[self.leading_index].inverse()
                return ExField([ e*x for x in self.coeffs ])

        def is_monic(self):
            return self.coeffs[self.leading_index]==1

        def is_zero(self):
            return self == ExField.zero()

        def is_one(self):
            return self == ExField.one()

        '''
        def inverse(self):
            print(ExField.mod_init(MOD))
            gcd, e, f = ExField.ext_euclid(self,MOD)
            if not gcd.is_one():
                print(f"GCD is not exist:{gcd},{e},{f}")
                return ExField.zero()
            else:
                return e
        '''

        @classmethod
        def zero(cls):
            return cls([0]*order)

        @classmethod
        def one(cls):
            return cls([0]*(order-1)+[1])

        
    return ExField




if __name__ == "__main__":
    print(0)



'''
        def shift_degree(self,i):
            assert self.degree+i<order 
            shifted = self.coeffs[i:]+(0,)*i
            return ExField(list(shifted))

        def __mod__(self, other):
            reminder = self

            # m次元多項式をn次元多項式未満の次元になるまで割り算する.よってm-n+1回割り算する。
            for i in reversed(range(self.degree-other.degree+1)):

                # 筆算で商を計算するまで
                div = reminder.coeffs[reminder.leading_index] / other.coeffs[other.leading_index]
                shift_other = other.shift_degree(i)
                temp = ExField([ div*x for x in shift_other.coeffs ])

                # 計算した商を引いて、余りを求める
                reminder = reminder - temp
            
            return reminder 

        def __floordiv__(self, other):
            reminder = self
            division = ExField.zero()

            # m次元多項式をn次元多項式未満の次元になるまで割り算する.よってm-n+1回割り算する。
            for i in reversed(range(self.degree-other.degree+1)):

                # 筆算で商を計算するまで
                div = reminder.coeffs[reminder.leading_index] / other.coeffs[other.leading_index]
                shift_other = other.shift_degree(i)
                temp = ExField([ div*x for x in shift_other.coeffs ])
                division += ExField([0]*(order-1)+[div]).shift_degree(i)

                # 計算した商を引いて、余りを求める
                reminder = reminder - temp
            
            return division
        #MODは次元が上限を超えるため、modを分ける必要があった。
        @classmethod
        def mod(cls,coeffs,m):
            if len(coeffs)<len(m):
                return coeffs

            reminder = coeffs
            poly = (len(coeffs)-len(m)) * (Fp(0),) + m

            # m次元多項式をn次元多項式未満の次元になるまで割り算する.よってm-n+1回割り算する。
            #for i in reversed(range((len(coeffs)-1)-order+1)):

            lr=math_util.find_non_zero_index(reminder)
            lp=math_util.find_non_zero_index(poly)

            # polyの次数以下となったらループを終了
            while lr<=lp:

                div = reminder[lr] / poly[lp]
                shifted = poly[(lp-lr):]+(Fp(0),)*(lp-lr)
                temp = tuple([div*x for x in shifted])

                # 計算した商を引いて、余りを求める
                reminder = tuple([x-y for x,y in zip(reminder,temp)])

                lr=math_util.find_non_zero_index(reminder)

            
            return  reminder[len(reminder)-order:]

        @classmethod
        def div(cls,coeffs,m):
            if len(coeffs)<len(m):
                return coeffs

            quotient = list(cls.zero().coeffs)
            reminder = coeffs
            poly = (len(coeffs)-len(m)) * (Fp(0),) + m

            lr=math_util.find_non_zero_index(reminder)
            lp=math_util.find_non_zero_index(poly)

            # polyの次数以下となったらループを終了
            while lr<=lp:

                div = reminder[lr] / poly[lp]
                shifted = poly[(lp-lr):]+(Fp(0),)*(lp-lr)
                temp = tuple([div*x for x in shifted])

                # 計算した商を引いて、余りを求める
                quotient[-(lp-lr)-1] = Fp(div)
                reminder = tuple([x-y for x,y in zip(reminder,temp)])

                lr=find_non_zero_index(reminder)
            
            return  quotient[len(quotient)-order:] 

        @classmethod
        def ext_euclid(cls,a,b):
            x = cls.one()
            y = cls.zero()
            nx = cls.zero()
            ny = cls.one()

            while not b.is_zero():
                q = a // b
                r = a % b

                tmpx = x - q*nx
                tmpy = y - q*ny

                a=b
                b=r
                x=nx
                y=ny
                nx=tmpx
                ny=tmpy

            return a.monic(),x.monic(),y.monic()
            #return b.monic(),nx.monic(),ny.monic()

        @classmethod
        def gcd(cls,lhs,rhs):
            if rhs.is_zero():
                return lhs.monic()

            reminder = lhs % rhs
            return cls.gcd(rhs ,reminder)

'''