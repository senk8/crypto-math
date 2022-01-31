import math

def init_comb(g, l, h, v, a, b):
    """
        l: l is bit lengh of e.
    """
    t = l - 1

    if h < 1 or t + 1 < h:
        raise ValueError("h is invalid value.")

    if v < 1 or a < v:
        raise ValueError("v is invalid value.")

    assert a*h >= t+1

    # step 1
    gs = [  g ** ( 2 ** (i * a) ) for i in range(0,h)]

    G = [ [ g.one() for _ in range(0, 2**h )] for _ in range(0, v) ]

    # step 2
    for i in range(1, 2**h):
        indexs = decimal_to_list_with_base(i, 2, h)

        # step 2.1
        acc = g.one()
        for j in range(0, h):
            acc *= gs[j] ** indexs[j]
        G[0][i] = acc

        # step 2.2
        for j in range(1, v) :
            exp = 2 ** (j * b)
            G[j][i] = G[0][i] ** exp

    def f(e):
        e = decimal_to_list_with_base(e, 2, h * a)

        I = [0] * a
        for i in range(0,a):
            for j in range(0,h):
                k = i + a * j
                I[i] += e[k] * (2 ** j)

        A = g.one()
        for k in range(b-1, -1, -1):
            A *= A 
            for j in range(v-1, -1, -1) :
                # j*b+kがaを以上にはならない。
                print(G)
                print(I)
                print(j)
                print(b)
                print(k)
                print(j*b+k)
                A = G[j][I[j*b+k]] * A			

        return A

    return f