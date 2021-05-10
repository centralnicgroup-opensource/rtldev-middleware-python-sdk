#!/usr/bin/env python

import os
import io
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as fh:
    long_description = fh.read()

PACKAGE = "hexonet.apiconnector"
VERSION = find_version("hexonet", "apiconnector", "__init__.py")

setup(
    name=PACKAGE,
    version=VERSION,
    description=PACKAGE
    + " is a connector library for the insanely fast HEXONET Backend API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kai Schwarz",
    author_email="kschwarz@hexonet.net",
    maintainer="Kai Schwarz",
    maintainer_email="kschwarz@hexonet.net",
    url="https://github.com/hexonet/python-sdk/",
    install_requires=[
        "docutils==0.*",
        "guzzle-sphinx-theme==0.*",
        "m2r2==0.*",
        "pytest-cov>=2,<4",
        "sphinx>=3,<5",
        "sphinxcontrib-log-cabinet==1.*",
        "sphinxcontrib-websupport==1.*",
        "twine==3.*",
        "black",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    license="MIT",
    scripts=[],
    zip_safe=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    namespace_packages=["hexonet"],
    packages=find_packages(),
    dependency_links=["git+git://github.com/psf/black.git@stable#egg=black"],
)
