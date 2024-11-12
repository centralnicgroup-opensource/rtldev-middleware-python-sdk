#!/bin/bash

# This script uploads the distribution packages to the Test PyPI repository.
# It uses the environment variables TWINE_TEST_USERNAME and TWINE_TEST_PASSWORD for authentication.

# TWINE_TEST_USERNAME: The username for Test PyPI.
# TWINE_TEST_PASSWORD: The password for Test PyPI.

# Increment the version number in your setup.py or pyproject.toml file before running this script.
# Example for setup.py: update the version parameter in the setup() function.
# Example for pyproject.toml: update the version field under [tool.poetry].

twine upload -u "${TWINE_TEST_USERNAME}" -p "${TWINE_TEST_PASSWORD}" --repository-url https://test.pypi.org/legacy/ dist/* --skip-existing