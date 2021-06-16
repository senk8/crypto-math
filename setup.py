from setuptools import setup,Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules = [Extension(
    # The cython file should always contain the same name as the extension module name.
    "crypto_math",sources=[
        "cython/crypto_math.pyx",
    ],
    language="c++",
),
]

setup(
    name="cytpto_math",
    ext_modules = cythonize(ext_modules),
    cmdclass={"build_ext": build_ext}
)