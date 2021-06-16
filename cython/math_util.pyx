def find_non_zero_index(seq):
    for i,x in enumerate(seq):
        if x!=0:
            return i
    return len(seq)-1

def padding(coeffs,n,Fp=int):
    deg = len(coeffs)-1
    if deg < n:
        return (n-deg) * (Fp(0),) + coeffs
    else :
        return coeffs

def pow_2_at_least(d):
    return 1 << len(bin(d))-2