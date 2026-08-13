# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ABRLFD User Manual'
copyright = '2026, Michael Baker International'
author = 'Michael Baker International'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_show_sphinx = False  


html_theme_options = {
    "footer_icons": [],
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for LaTeX output ------------------------------------------------

latex_documents = [
    (
        'index',
        'ablrfd-user-manual.tex',
        'ABLRFD User Manual',
        'Michael Baker International',
        'manual',
    ),
]

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{charter}
\usepackage[T1]{fontenc}
\DeclareUnicodeCharacter{2003}{\quad}
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03C6}{\ensuremath{\varphi}}
\setcounter{secnumdepth}{-1}
''',
    'figure_align': 'H',
}