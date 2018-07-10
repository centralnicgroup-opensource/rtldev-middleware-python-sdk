#!/bin/bash
pycodestyle --first --show-source --show-pep8 setup.py hexonet/apiconnector/__init__.py hexonet/apiconnector/connection.py hexonet/apiconnector/response.py hexonet/apiconnector/util.py
