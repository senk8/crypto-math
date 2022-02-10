import numbers
from xml.etree.ElementInclude import include
from setuptools import setup,Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from Cython.Compiler.Options import get_directive_defaults
import sys
import numpy

includes = sys.path 
includes.append(numpy.get_include())

#directive_defaults = get_directive_defaults()
#directive_defaults['linetrace'] = True
#directive_defaults['binding'] = True

ext_modules = [ Extension(
    # The cython file should always contain the same name as the extension module name.
    "crypto_math",sources=[
        "src/crypto_math.pyx",
    ],
    language="c++",
    include_dirs= includes, 
    libraries=['gmp', 'mpfr', 'mpc'],
    #define_macros=[('CYTHON_TRACE', '1')]
),
]

setup(
    name="crypto_math",
    version="0.0.1",
    ext_modules = cythonize(ext_modules, include_path=sys.path),
    cmdclass={"build_ext": build_ext},
    install_require = ["numpy", "gmpy2", "sympy", "pytest", "pytest-benchmark"],
    #compiler_directives={'profile': True, 'linetrace': True, 'binding': True},
)