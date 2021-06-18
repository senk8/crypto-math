from libcpp.vector cimport vector

cdef inline vector[int] mul_helper(lhs:tuple,rhs:tuple):
    cdef:
        int k
        int i
        vector[int] new_coeffs
        int ld = len(lhs) - 1
        int rd = len(rhs) - 1
        int d = ld + rd

    # ちゃんとゼロで初期化されるだろうか 
    new_coeffs.resize(d+1)
    
    for k in range(d+1):
        for i in range(k+1):
            if ld-i < 0 or rd- (k - i) < 0:
                continue
                    
            new_coeffs[d-k] += lhs[ld-i] * rhs[rd-(k-i)]
     
    return new_coeffs
