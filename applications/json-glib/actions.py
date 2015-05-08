#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    options = "-DCMAKE_BUILD_TYPE=Release \
               -DCMAKE_INSTALL_PREFIX=/usr \
               -DJSONCPP_LIB_BUILD_SHARED=ON \
               -DJSONCPP_WITH_TESTS=OFF
              "
               
    if get.buildTYPE() == "_emul32":
        options += "-DJSONCPP_LIB_DIR=/usr/lib32"
        
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    cmake.configure(options)

def build():
    cmake.make()

def install():
    cmake.rawInstall("DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "_emul32":
        pisitools.removeDir("/_emul32")

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("ChangeLog", "NEWS")
