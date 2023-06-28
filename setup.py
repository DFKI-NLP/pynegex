#!/usr/bin/env python
# from distutils.core import setup
import os
from setuptools import Extension, find_packages, setup

cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, "src/pynegex", "VERSION")) as fin:
    version = fin.read().strip()

setup(
    name='pynegex',
    version=version,
    author="Moe Bin Sumait",
    author_email="mh.binsumait@gmail.com",
    description="Pypi package for negex with multilingual support",
    # Find packages under the 'src' directory
    packages=find_packages(where='src'),
    package_dir={'': 'src'},              # Root directory for the packages
    py_modules=["pynegex"],                # Name of the python package
    # List any dependencies required by your package)
    python_requires='>=3.6',                # Minimum version requirement of the package
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],

)
