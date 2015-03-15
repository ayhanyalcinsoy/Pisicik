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
    cmaketools.configure("-DPORT=GTK \
                          -DENABLE_WEBKIT2=OFF \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIB_INSTALL_DIR=/usr/lib \
                          -DLIBEXEC_INSTALL_DIR=/usr/libexec/webkit2gtk-4.0 \
                          -DENABLE_GTKDOC=OFF \
                          -DHARFBUZZ_ICU_LIBRARIES=/usr/lib/libharfbuzz-icu.so \
                          -DFREETYPE2_HEADER_DIR=/usr/include/freetype2")

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())

