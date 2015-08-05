#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=/usr/lib -DCMAKE_BUILD_TYPE=release -DUSE_QT5=ON -DUSE_ENCA=ON", sourceDir="..")

    #pisitools.dosed("CMakeCache.txt", "LIB_INSTALL_DIR:PATH=/usr/lib64", "LIB_INSTALL_DIR:PATH=/usr/lib")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("COPYING","README","ChangeLog")
