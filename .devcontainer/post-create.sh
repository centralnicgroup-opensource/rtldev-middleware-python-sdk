#!/usr/bin/env zsh
# shellcheck shell=bash
# Python dependency install for this repository.
#
# Runs after the devbase Feature's own post-create, so pnpm, the global packages
# and the package.json dependencies are already in place. Everything the previous
# version of this script did besides the pip steps -- installing pnpm and the
# global packages, sourcing ~/.zshrc, symlinking ~/.gitconfig and ~/.zsh_history
# out of /WSL_USER -- is devbase's job now.
set -e

echo "=> Upgrading pip and installing pip-tools"
pip install --upgrade pip setuptools pip-tools

echo "=> Compiling requirements.txt from pyproject.toml"
pip-compile pyproject.toml

echo "=> Installing dependencies"
pip install -r requirements.txt

echo "=> Installing centralnicreseller as an editable package"
pip install -e .
