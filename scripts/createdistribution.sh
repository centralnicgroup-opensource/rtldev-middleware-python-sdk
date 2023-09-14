#!/bin/bash
rm -rf build dist
# python setup.py sdist bdist_wheel
python3 -m build --sdist .
