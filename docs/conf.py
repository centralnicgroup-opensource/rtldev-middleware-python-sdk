# -*- coding: utf-8 -*-

import sys
sys.path.append('~/.local/lib')

# Project --------------------------------------------------------------

project = 'hexonet.apiconnector'
copyright = '2018 by HEXONET GmbH'
author = 'Anthony Schneider, Kai Schwarz'
release = '1.2'
version = '1.2.6'

# General --------------------------------------------------------------

master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.log_cabinet'
]
exclude_patterns = ['_build', '/docs/api/*.rst']

source_suffix = ['.rst']

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