QR Code generator for Inkscape
==============================

While Inkscape provides a QR Code generator, this extension provides slightly
more options (i.e. generation of Micro QR Codes and an optimal error correction
level) and should be standard-conform.

This Inkscape extension includes `Segno <https://github.com/heuer/segno/>`_, a
BSD-licensed, pure Python library which implements the ``ISO/IEC 18004:2015(E)``
standard for QR Codes.


Installation
------------

Download the source distribution, extract it an copy ``inkscape_qrcode.inx`` and
the ``inkscape_qrcode`` directory into the target directoy (see below).

The QR Code generator should appear in the menu
``Extensions > Render > Barcode > QR Code (Segno)``



Inkscape extension path
-----------------------

OS X
^^^^
* global: /Applications/Inkscape.app/Contents/Resources/extensions
* local: $HOME/.config/inkscape/extensions


Linux
^^^^^
* global: /usr/share/inkscape/extensions
* local: $HOME/.config/inkscape/extensions


Windows
^^^^^^^
* global: C:\\Program Files\\Inkscape\\share\\extensions
* local: C:\\Documents and Settings\\User\\Application Data\\Inkscape\\extensions
