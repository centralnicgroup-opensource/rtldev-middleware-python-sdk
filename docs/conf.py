# -*- coding: utf-8 -*-

import sys
import os
import io
import re
sys.path.append('~/.local/lib')


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# Project --------------------------------------------------------------


project = 'hexonet.apiconnector'
copyright = '2018 by HEXONET GmbH'
author = 'Anthony Schneider, Kai Schwarz'
version = find_version('..', 'hexonet', 'apiconnector', '__init__.py')
release = re.sub(r"\.[0-9]+$", "", version)

# General --------------------------------------------------------------

master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.log_cabinet',
    'm2r2'
]
exclude_patterns = ['_build', '/docs/api/*.rst']

source_suffix = ['.rst', '.md']

intersphinx_mapping = {}

# HTML -----------------------------------------------------------------
import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "https://rawgit.com/hexonet/python-sdk/master/docs/",
    "project_nav_name": "hexonet.apiconnector " + version
}

html_sidebars = {
    '**': [
        'logo-text.html',
        'globaltoc.html',
        'localtoc.html',
        'searchbox.html'
    ]
}

html_static_path = ['_static']
html_favicon = '_static/hexonet-favicon.ico'
html_logo = '_static/hexonet.png'
html_show_sourcelink = True

# linkcheck ------------------------------------------------------------

linkcheck_anchors = False
