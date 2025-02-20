#!/bin/bash
# NOTE: This file will be executed as remoteUser (devcontainer.json)
echo "=> Script: post-create.sh Executed by: $(whoami)"

npm install --silent --global gulp-cli commitizen@latest cz-conventional-changelog@latest

# shellcheck source=/dev/null
source ~/.zshrc

pip install --upgrade pip
pip install --upgrade setuptools
pip -V

# Install pip-tools
pip install pip-tools

# Generate requirements.txt from pyproject.toml
pip-compile pyproject.toml

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install the local centralnicreseller module as an editable package
pip install -e .

echo "=> Generating Symlinks for Zsh History and Git config"
# Create symlink for gitconfig and zsh history file
if [[  ! -L "${HOME}/.gitconfig" ]]; then
    ln -s "/WSL_USER/.gitconfig" "${HOME}/.gitconfig"
fi

if [[  ! -L "${HOME}/.zsh_history" ]]; then
    ln -s "/WSL_USER/.zsh_history" "${HOME}/.zsh_history"
fi