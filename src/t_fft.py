import fft

def discrete_fourier_transform(poly,n):
    unity = fft.get_unity(n)
    new_poly = [fft.f(poly,unity**i,n) for i in range(n)]
    return new_poly

def inverse_discrete_fourier_transform(poly,n):
    unity = fft.get_unity(n)**(-1)
    new_poly = [1/n*fft.f(poly,unity**i,n) for i in range(n)]
    return new_poly

