import math

def decimal_to_list_with_base(n, base, t):
    res = [0]*(t+1)
    i = 0

    for i in range(0,t+1):
        res[i] = n%base
        n //= base
        if 0 >= n:
            break 

    return res


# h**(t+1) までの値を計算できる
# h**l
def init_windowing(g, h, l): 
    """
        m = range of value. For example, you would like to include 1024bit number, then you specify m = 2**1024;
    """
    b = h
    t = l - 1
    gs = [ g ** (b ** i) for i in range(0, t+1) ]

    if 2 > b:
        raise ValueError('b is lower than 2')

    # t + h - 2
    def f(exp):
        es = decimal_to_list_with_base(exp, b, t)
        A = 1
        B = 1
        for j in range(h-1, 0, -1):
            for i,e in enumerate(es):
                if e == j:
                    B *= gs[i]
            A *= B 

        return A

    return f
