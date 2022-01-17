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


def init_windowing(g,h,m): 
    """
        m = range of value. For example, you would like to include 1024bit number, then you specify m = 2**1024;
    """
    b = h
    t = math.ceil(math.log(m,b)) - 1
    gs = [ g ** (b ** i) for i in range(0, t) ]

    def f(e):
        es = decimal_to_list_with_base(e,b)
        A = 1
        B = 1
        for j in range(h-1,0):
            for i in range(0,t):
                if es[i] == j:
                    B *= gs[i]
            A *= B 

        return A

    return f
