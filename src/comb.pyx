def precomputation(g, t, h, v, a, b):
    """
        t: t-1 is bit lengh of e.
    """
    if h < 1 or t + 1 < h:
        raise ValueError("h is invalid value.")

    if v < 1 or a < v:
        raise ValueError("v is invalid value.")

    print("Step 1: Start")

    # step 1
    gs = [0] * h
    for i in range(0,h): 
        gs[i] = g ** ( 2 ** (i * a) )

    G = [ [1 for _ in range(0, 2**h )] for _ in range(0, v) ]

    print("Step 1: Done")

    print("Step 2: Start")

    # step 2
    for i in range(1, 2**h):
        indexs = decimal_to_list_with_base(i, 2, h)

        # step 2.1
        acc = 1
        for j in range(0, h):
            acc *= gs[j] ** indexs[j]
        G[0][i] = acc

        print("Step 2.1: Done")

        # step 2.2
        for j in range(1, v) :
            exp = 2 ** (j * b)
            G[j][i] = G[0][i] ** exp

        print("Step 2.2: Done")


    print("Step 2: Done")

    return G

# tがビット長
def comb(h, v, a, b, G, e):
    e = decimal_to_list_with_base(e, 2, h * a)

    # EをIの列に変換する
    I = [0] * a
    for i in range(0,a):
        for j in range(0,h):
            k = i + a * j
            I[i] += e[k] * (2 ** j)

    A = 1
    for k in range(b-1, -1, -1):
        A *= A 
        for j in range(v-1, -1, -1):
            A = G[j][I[j*b+k]] * A			

    return A