from setuptools import setup,Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules = [Extension(
    # The cython file should always contain the same name as the extension module name.
    "crypto_math",sources=[
        "src/crypto_math.pyx",
    ],
    language="c++",
),
]

setup(
    name="cytpto_math",
    version="0.0.1",
    ext_modules = cythonize(ext_modules),
    cmdclass={"build_ext": build_ext}
)