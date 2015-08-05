#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                          -DUSE_QT5=ON \
                          -DNETWORKMONITOR_PLUGIN=yes \
                          -DCMAKE_BUILD_TYPE=release", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/=/usr/share/cmake", "/usr/share")
    pisitools.removeDir("/usr/=")
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "COPYING")
