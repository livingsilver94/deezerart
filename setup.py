import os
import shutil

from setuptools import Command, find_packages, setup

import deezerart

deps = open('requirements.txt').readlines()
test_deps = open('requirements.tests.txt').readlines()


class MkpluginCommand(Command):
    description = 'create a deezerart.zip plugin file'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for dirname, subdirs, _files in os.walk('deezerart'):
            if '__pycache__' in subdirs:
                shutil.rmtree(os.path.join(dirname, '__pycache__'))
        shutil.make_archive('deezerart', 'zip', root_dir='.', base_dir='deezerart')


setup(
    name='deezerart',
    version=deezerart.__version__,

    packages=find_packages(),

    python_requires='>=3.5',
    install_requires=deps,
    tests_require=test_deps,

    cmdclass={
        "mkplugin": MkpluginCommand,
    },
)
