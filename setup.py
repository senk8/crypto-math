from setuptools import setup,Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

#import os
#os.environ['CC'] = 'g++'
#os.environ['CXX'] = 'g++'

ext_modules = [Extension(
    "galois_field",sources=["cython/galois_field.pyx"],
    language="c++",
),
]


setup(
    name="galois_field",
    ext_modules = cythonize(ext_modules),
    cmdclass={"build_ext": build_ext}
)