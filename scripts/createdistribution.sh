#!/bin/bash
rm -rf build dist
python setup.py sdist bdist_wheel
