#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules


def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DBUILD_TESTS=OFF \
                          -DPYTHON_EXECUTABLE=/usr/bin/python \
                          -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
                          -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
                          -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=yes")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
