#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Greynir documentation build configuration file, created by
# sphinx-quickstart on Sun Apr  8 01:20:08 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

from typing import TYPE_CHECKING, Mapping, Any

import os
from datetime import datetime

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
year = datetime.now().year
project = "Greynir"
copyright = "{0} Miðeind ehf".format(year)
author = "Miðeind ehf."

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Get version string from "../src/reynir/version.py"
basepath, _ = os.path.split(os.path.realpath(__file__))
version_path = os.path.join(basepath, "..", "src", "reynir", "version.py")

if TYPE_CHECKING:
    __version__ = ""
else:
    exec(open(version_path).read())

# The full version, including alpha/beta/rc tags.
release = __version__  # pylint: disable=undefined-variable
# The short X.Y version.
version = ".".join(__version__.split(".")[:2])  # pylint: disable=undefined-variable

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_sidebars = {
    "**": ["about.html", "navigation.html", "relations.html", "searchbox.html"]
}
html_theme_options: Mapping[str, Any] = {
    "logo": "GreynirLogo400.png",
    "logo_name": False,
    "logo_text_align": "center",
    "description": "Natural Language Processing for Icelandic",
    "github_user": "mideind",
    "github_repo": "GreynirEngine",
    "github_button": True,
    "sidebar_collapse": False,
    "fixed_sidebar": True,
    "font_family": (
        "Lato, Georgia, 'goudy old style', 'minion pro', "
        "'bell mt', 'Hiragino Mincho Pro', serif"
    ),
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Set the favicon
html_favicon = "_static/greynir-favicon-32x32.png"

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Greynirdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    "preamble": "",
    # Latex figure (float) alignment
    "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "Greynir.tex", "Greynir Documentation", "Miðeind ehf.", "manual")
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "greynir", "Greynir Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Greynir",
        "Greynir Documentation",
        author,
        "Greynir",
        "Natural language processing for Icelandic",
        "NLP",
    )
]