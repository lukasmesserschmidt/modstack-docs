# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "ModStack"
copyright = "2025, Lukas Messerschmidt"
author = "Lukas Messerschmidt"

release = "0.1"
version = "1.0.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "furo"

html_logo = ""

html_title = f"ModStack {version} Documentation"

# -- Options for EPUB output
epub_show_urls = "footnote"
