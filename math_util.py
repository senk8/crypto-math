import copy as cp

def find_non_zero_index(seq):
    for i,x in enumerate(seq):
        if x!=0:
            return i
    return len(seq)-1

def align_coeffs(Fp,arg1,arg2):

    if arg1.degree < arg2.degree:
        arg1 = cp.deepcopy(arg1)
        arg1.coeffs = (arg2.degree-arg1.degree)*(Fp(0),)+arg1.coeffs
    elif arg2.degree < arg1.degree:
        arg2 = cp.deepcopy(arg2)
        arg2.coeffs = (arg1.degree-arg2.degree)*(Fp(0),)+arg2.coeffs

    return arg1,arg2