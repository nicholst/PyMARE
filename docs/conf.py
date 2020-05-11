#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PyMARE documentation build configuration file, created by
# sphinx-quickstart
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
import os
import sys
from datetime import datetime
sys.path.insert(0, os.path.abspath('sphinxext'))
sys.path.insert(0, os.path.abspath(os.path.pardir))

from github_link import make_linkcode_resolve

import pymare


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

# needs_sphinx = '1.0'

# generate autosummary even if no references
autosummary_generate = True
autodoc_default_flags = ['members', 'inherited-members']
add_module_names = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.doctest',
              'sphinx.ext.ifconfig',
              'sphinx.ext.intersphinx',
              'sphinx.ext.linkcode',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'sphinx.ext.todo',
              'sphinx_copybutton',
              'sphinx_gallery.gen_gallery',
              'sphinxarg.ext',
              'm2r',
              'numpydoc']

import sphinx
from distutils.version import LooseVersion
if LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
    extensions.append('sphinx.ext.pngmath')
else:
    extensions.append('sphinx.ext.imgmath')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyMARE'
copyright = '2018-' + datetime.today().strftime("%Y") + ', PyMARE developers'
author = 'PyMARE developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pymare.__version__
# The full version, including alpha/beta/rc tags.
release = pymare.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'utils/*']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "autolink"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# installing theme package

import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'searchbox.html', 'indexsidebar.html'] }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# https://github.com/rtfd/sphinx_rtd_theme/issues/117
def setup(app):
    app.add_stylesheet('theme_overrides.css')
    app.add_stylesheet('pymare.css')
    app.connect('autodoc-process-docstring', generate_example_rst)

html_favicon = '_static/nimare_favicon.png'
html_logo = '_static/nimare_banner.png'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pymaredoc'

# The following is used by sphinx.ext.linkcode to provide links to github
linkcode_resolve = make_linkcode_resolve('pymare',
                                         u'https://github.com/neurostuff/'
                                         'pymare/blob/{revision}/'
                                         '{package}/{path}#L{lineno}')

# -----------------------------------------------------------------------------
# intersphinx
# -----------------------------------------------------------------------------
_python_version_str = '{0.major}.{0.minor}'.format(sys.version_info)
_python_doc_base = 'https://docs.python.org/' + _python_version_str
intersphinx_mapping = {
    'python': (_python_doc_base, None),
    'numpy': ('https://docs.scipy.org/doc/numpy',
              (None, './_intersphinx/numpy-objects.inv')),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference',
              (None, './_intersphinx/scipy-objects.inv')),
    'sklearn': ('https://scikit-learn.org/stable',
                (None, './_intersphinx/sklearn-objects.inv')),
    'matplotlib': ('https://matplotlib.org/',
                   (None, 'https://matplotlib.org/objects.inv')),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
}

sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs'     : '../examples',
    # path where to save gallery generated examples
    'gallery_dirs'      : 'auto_examples',
    'backreferences_dir': 'generated',
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    'doc_module'        : ('pymare',),
    'ignore_patterns'   : ['utils/'],
    'reference_url': {
         # The module you locally document uses None
        'pymare': None,
        'matplotlib': 'https://matplotlib.org/',
        'numpy': 'http://docs.scipy.org/doc/numpy/',
    },
}

# Generate the plots for the gallery
plot_gallery = 'True'

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'project-template', u'project-template Documentation',
   u'Vighnesh Birodkar', 'project-template', 'One line description of project.',
   'Miscellaneous'),
]

def generate_example_rst(app, what, name, obj, options, lines):
    # generate empty examples files, so that we don't get
    # inclusion errors if there are no examples for a class / module
    folder = os.path.join(app.srcdir, 'generated')
    if not os.path.isdir(folder):
        os.makedirs(folder)
    examples_path = os.path.join(app.srcdir, "generated",
                                 "%s.examples" % name)
    if not os.path.exists(examples_path):
        # touch file
        open(examples_path, 'w').close()

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False
