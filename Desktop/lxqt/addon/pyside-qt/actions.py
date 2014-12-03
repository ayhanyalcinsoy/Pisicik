#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
#from pisi.actionsapi import pisitools


def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
			  -DUSE_QTMIMETYPES=OFF \
			  -DBUILD_TESTS=OFF \
			  -DQT_PHONON_INCLUDE_DIR=/usr/include/qt4/phonon \
			  -DQT_QMAKE_EXECUTABLE=qmake-qt4")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
