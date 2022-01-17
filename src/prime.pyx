from sympy import isprime

def get_prime(bit):
    begin = 1 << (bit - 1)
    end = 1 << bit 
    for i in range(begin,end):
        if isprime(i):
            return i

def get_safe_prime(bit):
    begin = 1 << (bit - 1)
    end = 1 << bit 
    for i in range(begin,end):
        if is_safe_prime(i):
            return i
    exit(1)

def is_safe_prime(prime):
    if isprime(prime):
        if isprime((prime - 1)//2):
            return True
        else :
            return False
    return False
