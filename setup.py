from setuptools import find_packages, setup

import deezerart

setup(
    name=deezerart.__name__,
    version=deezerart.__version__,

    packages=find_packages(),

    python_requires='>=3.5',
)
