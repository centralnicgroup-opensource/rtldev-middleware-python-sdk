#!/bin/bash
rm -rf docs/_build/html
wget -q -t 3 -O ./docs/app.py https://raw.githubusercontent.com/centralnicgroup-opensource/rtldev-middleware-python-sdk-demo/master/app.py
sphinx-apidoc -fMETa -d 2 --implicit-namespaces -o ./docs/api hexonet
cd docs || exit
make html
cd .. || exit
