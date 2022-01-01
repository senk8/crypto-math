from crypto_math import GF,field_extension

F2 =GF(2)
x = field_extension(F2,4)

g=x.generator()

print(g)