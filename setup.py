#!/usr/bin/env python
# from distutils.core import setup
import os
from setuptools import Extension, find_packages, setup
from pathlib import Path
cwd = Path(__file__).parent

long_description = (cwd / "README.md").read_text()

# cwd = os.path.dirname(os.path.abspath(__file__))
# with open(os.path.join(cwd, "src/pynegex", "VERSION")) as fin:
#     version = fin.read().strip()
setup(
    name='pynegex',
    version="0.0.2-dev",
    author="Moe Bin Sumait",
    author_email="mh.binsumait@gmail.com",
    description="Pypi package for negex with multilingual support",
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Find packages under the 'src' directory
    packages=find_packages(where='src'),
    # Root directory for the packages
    package_dir={'pynegex': 'src'},
    package_data={'pynegex': [
        "src/pynegex/VERSION",
        "src/pynegex/model/triggersets/*.txt"
    ]},
    py_modules=["pynegex"],                # Name of the python package
    # List any dependencies required by your package)
    python_requires='>=3.6',                # Minimum version requirement of the package
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],

)
