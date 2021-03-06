#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
del os.link
from importlib import import_module

try:
    from setuptools import setup, find_packages
except:
    sys.exit("Error: missing python-setuptools library")

try:
    python_version = sys.version_info
except:
    python_version = (1, 5)
if python_version < (2, 7):
    sys.exit("This application requires a minimum Python 2.7.x, sorry!")
elif python_version >= (3,):
    sys.exit("This application is not yet compatible with Python 3.x, sorry!")

from babel_bottle import __application__, __version__, __copyright__
from babel_bottle import __releasenotes__, __license__, __doc_url__
from babel_bottle import __name__ as __pkg_name__

package = import_module('babel_bottle')

setup(
    name=__pkg_name__,
    version=__version__,

    license=__license__,

    # metadata for upload to PyPI
    author="Frédéric MOHIER",
    author_email="frederic.mohier@gmail.com",
    keywords="babel bottle gettext",
    url="https://github.com/mohierf/babel-bottle",
    description=package.__doc__.strip(),
    long_description=open('README.rst').read(),

    zip_safe=False,

    packages=find_packages(),
    include_package_data=True,

    entry_points = """
    [babel.extractors]
    tpl = babel_bottle:extract_tpl
    """,

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration'
    ]
)