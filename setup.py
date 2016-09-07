#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Inkscape QR Code
# Copyright (C) 2016 Lars Heuer
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public
# License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
"""\
Setup script.
"""
from __future__ import unicode_literals
from setuptools import setup, find_packages
import os
import io
import re


def read(*filenames, **kwargs):
    base_path = os.path.dirname(os.path.realpath(__file__))
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(os.path.join(base_path, filename), encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

version = re.search(r'''^__version__ = ["']([^'"]+)['"]''',
                    read('inkscape_qrcode/qrcode.py'), flags=re.MULTILINE).group(1)

setup(
    name='inkscape-qrcode',
    version=version,
    url='https://github.com/heuer/inkscape-qrcode/',
    description='QR Code and Micro QR Code generator for Inkscape',
    long_description=read('README.rst', 'CHANGES.rst'),
    license='GPL2',
    author='Lars Heuer',
    author_email='heuer@semagia.com',
    platforms=['any'],
    packages=find_packages(),
    include_package_data=True,
    keywords=['QR Code', 'Micro QR Code', 'ISO/IEC 18004',
              'ISO/IEC 18004:2006(E)', 'ISO/IEC 18004:2015(E)', 'qrcode', 'QR',
              'barcode', 'matrix', '2D', 'Inkscape'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Printing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
