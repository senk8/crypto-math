# crypto_math

This is a full-scratch implementation of an algebraic structure for cryptology.


# Setup (Mac)

Install required libraries.

```
brew install gmp
pip install gmpy 
```


Building Cython 

```
$ python3 setup.py install
```

How to test crypto_math as follows:

```
$ export PYTHONPATH = cypto-math/src
$ pytest 
```

# Feature

For example, F_p^n. we call p degree, and call n order.

# Requirement

- Cython
- Python3
- numpy
- gmpy
