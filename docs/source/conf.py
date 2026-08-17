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
    'sphinx.ext.mathjax',
]

myst_enable_extensions = ["dollarmath"]

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
    'sphinxsetup': 'hmargin={0.85in,0.85in},vmargin={0.85in,0.85in}',
    'preamble': r'''
\usepackage{charter}
\usepackage[T1]{fontenc}
\usepackage{etoolbox}
\AtBeginEnvironment{tabulary}{\small}
\AtBeginEnvironment{longtable}{\small}
\AtBeginEnvironment{tabular}{\small}
\setlength{\tabcolsep}{2pt}
\setlength{\tymin}{55pt}
\DeclareUnicodeCharacter{2003}{\quad}
\DeclareUnicodeCharacter{2011}{-}
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03B2}{\ensuremath{\beta}}
\DeclareUnicodeCharacter{03B3}{\ensuremath{\gamma}}
\DeclareUnicodeCharacter{03B4}{\ensuremath{\delta}}
\DeclareUnicodeCharacter{03B5}{\ensuremath{\varepsilon}}
\DeclareUnicodeCharacter{03B7}{\ensuremath{\eta}}
\DeclareUnicodeCharacter{03B8}{\ensuremath{\theta}}
\DeclareUnicodeCharacter{03BA}{\ensuremath{\kappa}}
\DeclareUnicodeCharacter{03BB}{\ensuremath{\lambda}}
\DeclareUnicodeCharacter{03BC}{\ensuremath{\mu}}
\DeclareUnicodeCharacter{03C1}{\ensuremath{\rho}}
\DeclareUnicodeCharacter{03C3}{\ensuremath{\sigma}}
\DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}
\DeclareUnicodeCharacter{03C5}{\ensuremath{\upsilon}}
\DeclareUnicodeCharacter{03C6}{\ensuremath{\varphi}}
\DeclareUnicodeCharacter{0394}{\ensuremath{\Delta}}
\DeclareUnicodeCharacter{02DA}{\ensuremath{^\circ}}
\DeclareUnicodeCharacter{03BF}{o}
\DeclareUnicodeCharacter{2264}{\ensuremath{\leq}}
\DeclareUnicodeCharacter{2265}{\ensuremath{\geq}}
\setcounter{secnumdepth}{-1}
\usepackage{bookmark}
\bookmarksetup{
    numbered,
    open,
}
''',
    'figure_align': 'H',
}

# Control PDF bookmark depth
latex_toplevel_sectioning = 'chapter'

# Ensure bookmarks show only top-level headings for navigation sections
latex_show_pagerefs = False
latex_show_urls = 'footnote'