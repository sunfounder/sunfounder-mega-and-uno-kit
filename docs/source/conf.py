# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme
import time  

project = 'SunFounder uno-and-mega-kit'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# SunFounder logo

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
]

#### RTD+

# html_js_files = [
#     'https://ezblock.cc/readDocFile/custom.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',

# ]
# html_css_files = [
#     'https://ezblock.cc/readDocFile/custom.css',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
#     'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
# ]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.


# open link in a new window

rst_epilog = """

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">here</a>

.. |link_download_arduino| raw:: html

    <a href="https://www.arduino.cc/en/software#future-version-of-the-arduino-ide" target="_blank">Arduino IDE 2.0.0 Page</a>


.. |link_ascii| raw:: html

    <a href="https://www.asciitable.com/" target="_blank">ASCII table of characters</a>

.. |link_video_scott| raw:: html

    <a href="https://www.circuitbasics.com/ultimate-guide-to-the-arduino/" target="_blank">Ultimate Guide to Arduino</a>

.. |link_video_roboja| raw:: html

    <a href="https://www.youtube.com/playlist?list=PLHvJ4bw0xno5CYSnnLbPzdJYw7vXoNORj" target="_blank">Video Tutorials for Car Projects</a>

.. |link_video_roboja_iot| raw:: html

    <a href="hhttps://www.youtube.com/watch?v=qE1bkgziGXg&list=PLHvJ4bw0xno7Cjq3eRMIZo5YBNrL6NKgw&index=31" target="_blank">Video Tutorials for Car Projects</a>

.. |link_UNO_Starter_Kit| raw:: html

    <a href="https://www.sunfounder.com/products/unor3-project-starter-kit?_pos=2&_sid=15087482c&_ss=r" target="_blank">Purchase Link for UNO Starter Kit</a>

.. |link_UNO_Kit| raw:: html

    <a href="https://www.sunfounder.com/products/unor3-project-starter-kit?_pos=2&_sid=15087482c&_ss=r" target="_blank">UNO Starter Kit</a>

"""
