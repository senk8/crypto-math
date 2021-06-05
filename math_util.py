def find_non_zero_index(seq):
    for i,x in enumerate(seq):
        if x!=0:
            return i
    return len(seq)-1