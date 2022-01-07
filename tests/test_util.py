import crypto_math as gf


def test_enc(benchmark):
    n: int = 4
    p: int = 2
    Domain = gf.field_extension(gf.GF(p), n)
    benchmark(gf.enc, Domain((1, 1, 1)))
    for i, x in enumerate(Domain.enumerate()):
        assert i == gf.enc(Domain(x))


def test_enc2(benchmark):
    n: int = 4
    p: int = 2
    Domain = gf.field_extension(gf.GF(p), n)
    benchmark(gf.enc2, Domain((1, 1, 1)))
    for i, x in enumerate(Domain.enumerate()):
        assert i == gf.enc(Domain(x))
