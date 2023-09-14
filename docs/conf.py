# -*- coding: utf-8 -*-

import sys
import os
import io
import re

sys.path.append("~/.local/lib")


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Project --------------------------------------------------------------


project = "hexonet.apiconnector"
copyright = "2023 by HEXONET"
author = "Kai Schwarz"
version = find_version("..", "hexonet", "apiconnector", "__init__.py")
release = re.sub(r"\.[0-9]+$", "", version)

# General --------------------------------------------------------------

master_doc = "index"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "m2r2",
    "sphinx_rtd_theme"
]
exclude_patterns = ["_build", "/docs/api/*.rst"]

source_suffix = [".rst", ".md"]

intersphinx_mapping = {}

html_theme = "sphinx_rtd_theme"

# sphinx_rtd_theme config options
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#theme-options
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_static_path = ["_static"]
html_favicon = "_static/hexonet-favicon.ico"
html_logo = "_static/hexonet.png"
html_show_sourcelink = True

# linkcheck ------------------------------------------------------------

linkcheck_anchors = False
