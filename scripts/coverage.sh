#!/bin/bash
rm -rf .pytest_cache htmlcov tests/__pycache___
py.test --strict --cov-report html --cache-clear -v
# NOTE: this does not use the current repository
# it uses the last released version's source code
# maybe this can be reviewed - but not sure if this is possible
