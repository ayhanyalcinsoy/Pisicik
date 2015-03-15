#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    options = "--disable-static"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
    pisitools.dosed("Makefile.in","check: scripts/symbols.chk","check:")
    autotools.configure(options)
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    if get.buildTYPE() == "emul32":
        pisitools.dolib_so(".libs/libpng16.so.16.16.0", destinationDirectory = "/usr/lib32")
        pisitools.dosym("libpng16.so.16.16.0", "/usr/lib32/libpng16.so.16")
    else:
        pisitools.dolib_so(".libs/libpng16.so.16.16.0")
        pisitools.dosym("libpng16.so.16.16.0", "/usr/lib/libpng16.so.16")
