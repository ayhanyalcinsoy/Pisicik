#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib/sddm \
                          -DBUILD_MAN_PAGES=OFF \
                          -DUSE_QT5=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING")
 
