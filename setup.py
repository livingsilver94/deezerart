from setuptools import find_packages, setup

import deezerart

deps = open('requirements.txt').readlines()
test_deps = open('requirements.tests.txt').readlines()

setup(
    name=deezerart.__name__,
    version=deezerart.__version__,

    packages=find_packages(),

    python_requires='>=3.5',
    install_requires=deps,
    tests_require=test_deps,
)
