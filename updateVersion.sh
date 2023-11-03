#!/bin/bash

# THIS SCRIPT UPDATES THE HARDCODED VERSION
# IT WILL BE EXECUTED IN STEP "prepare" OF
# semantic-release. SEE package.json

# version format: X.Y.Z
newversion="$1"

printf -v sed_script 's/return "[0-9]\+\.[0-9]\+\.[0-9]\+"/return "%s"/g' "${newversion}"
sed -i -e "${sed_script}" hexonet/apiconnector/apiclient.py

printf -v sed_script 's/__version__ = "[0-9]\+\.[0-9]\+\.[0-9]\+"/__version__ = "%s"/g' "${newversion}"
sed -i -e "${sed_script}" hexonet/apiconnector/__init__.py

sed -i "s/version = \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/version = \"$newversion\"/g" "pyproject.toml"
