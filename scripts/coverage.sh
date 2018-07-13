#!/bin/bash
rm -rf .pytest_cache htmlcov tests/__pycache___
py.test --cov-report html --cov=hexonet.apiconnector tests/
