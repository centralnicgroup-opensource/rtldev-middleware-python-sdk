#!/bin/bash

# This script uploads the distribution packages to the Test PyPI repository.
# It uses the environment variables TWINE_TEST_USERNAME and TWINE_TEST_TOKEN for authentication.

# TWINE_TEST_USERNAME: The username for Test PyPI.
# TWINE_TEST_TOKEN: The password for Test PyPI.

# no user name is needed when using API tokens, so we can skip the username and just use the token for authentication.

# Increment the version number in your setup.py or pyproject.toml file before running this script.
# Example for setup.py: update the version parameter in the setup() function.
# Example for pyproject.toml: update the version field under [tool.poetry].

twine upload -p "${TWINE_TEST_TOKEN}" --repository-url https://test.pypi.org/legacy/ dist/* --skip-existing