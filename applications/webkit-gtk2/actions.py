#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("--disable-gtk-doc \
                         --disable-webkit2 \
                         --enable-introspection \
                         --enable-jit \
                         --enable-introspection \
                         --with-gtk=3.0 \
                         --prefix=/usr \
                         --libexecdir=/usr/lib/webkit-2.4.8")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

