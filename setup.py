import os
import setuptools
from pok.version import get_version, read_requirements

readme = open('README.md').read()
dependencies, requirements = read_requirements('requirements.txt')

long_description = """
pok %s
Configuration should be easy.

To install use pip install git+git://git@github.com:iPlantCollaborativeOpenSource/pok.git

----

%s

----

For more information, please see: https://github.com/iPlantCollaborativeOpenSource/pok
""" % (get_version('short'), readme)

setuptools.setup(
    name='pok',
    version=get_version('short'),
    author='jmatt',
    author_email='jmatt@jmatt.org',
    description="Configuration should be easy.",
    long_description=long_description,
    license="BSD 3 Clause",
    url="https://github.com/iPlantCollaborativeOpenSource/pok",
    packages=setuptools.find_packages(),
    dependency_links=dependencies,
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: System",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Systems Administration"
    ])
