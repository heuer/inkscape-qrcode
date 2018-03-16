#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Inkscape QR Code
# Copyright (C) 2016 - 2018 Lars Heuer
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
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""\
Helper script to update Segno to the latest version.
"""
from __future__ import absolute_import, unicode_literals, print_function
import json
import os
import re
import io
import tarfile
import shutil
try:
    unicode
    from io import open
except NameError:
    pass
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


_SEGNO_URL = 'https://pypi.python.org/pypi/segno/json'
_LINK_PATTERN = re.compile(r'<a href="([^"]+)"[^>]*>segno\-[0-9\.]+tar\.gz')
_VERSION_PATTERN = re.compile(r'''__version__\s+=\s+['"]([0-9\.]+)['"]''')
_VERSION_PATTERN_FILENAME = re.compile('segno-([0-9\.]+)\.tar\.gz')

_WANTED_FILES = ('consts.py', 'encoder.py', 'utils.py')


def update_segno():
    """\
    Downloads the latest Segno version and updates the "_segno" package.
    """
    segno_subdir = os.path.join(os.path.dirname(__file__), 'inkscape_qrcode', '_segno')
    with open(os.path.join(segno_subdir, '__init__.py')) as f:
        m = _VERSION_PATTERN.search((f.read()))
    segno_internal_version = m.group(1)
    resp = urlopen(_SEGNO_URL)
    if resp.getcode() != 200:
        raise Exception('Error retrieving the PyPi page: %s' % resp.getcode())
    j = json.loads(resp.read())
    download_url = None
    for urldct in j['urls']:
        if urldct['python_version'] == 'source':
            download_url = urldct['url']
            break
    current_version = _VERSION_PATTERN_FILENAME.search(download_url).group(1)
    if segno_internal_version == current_version:
        print('No update found. Current Segno version: "%s"' % segno_internal_version)
        return
    resp = urlopen(download_url)
    if resp.getcode() != 200:
        raise Exception('Download of package failed: %s' % resp.getcode())
    buff = io.BytesIO(resp.read())
    buff.seek(0)
    needed_files = list(_WANTED_FILES)
    with tarfile.open(fileobj=buff, mode='r:gz') as f:
        for member in f.getmembers():
            member_name = os.path.basename(member.name)
            if member_name in needed_files:
                mf = f.extractfile(member)
                needed_files.remove(member_name)
                with open(os.path.join(segno_subdir, member_name), 'wb') as fdst:
                    shutil.copyfileobj(mf, fdst)
                if not needed_files:
                    break
    if needed_files:
        print('Not all files found. Missing: %r' % needed_files)
        print("Don't forget to revert changes!")
        return
    segno_init_file = os.path.join(segno_subdir, '__init__.py')
    with open(segno_init_file, 'r') as f:
        s = f.read()
    s = s.replace(segno_internal_version, current_version)
    with open(segno_init_file, 'w') as f:
        f.write(s)
    inx_fn = os.path.join(os.path.dirname(__file__), 'inkscape_qrcode.inx')
    with open(inx_fn, 'r', encoding='utf-8') as f:
        s = f.read()
    s = s.replace('Segno %s' % segno_internal_version, 'Segno %s' % current_version)
    with open(inx_fn, 'w', encoding='utf-8') as f:
        f.write(s)
    print('Updated Segno from %s to %s' % (segno_internal_version, current_version))


if __name__ == '__main__':
    update_segno()
