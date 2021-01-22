#!/bin/bash
rm -rf .pytest_cache htmlcov tests/__pycache___
python setup.py test
# NOTE: this does not use the current repository
# it uses the last released version's source code
# maybe this can be reviewed - but not sure if this is possible
