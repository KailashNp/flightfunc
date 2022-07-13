from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Flightfunc i did for schl'


# Setting up
setup(
    name="flightfunc",
    version=VERSION,
    author="Kailash",
    author_email="<kailashnprasad@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pickle'],
    keywords=['python', 'pickle', 'kailash', 'flight', 'func', 'anilegend'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
