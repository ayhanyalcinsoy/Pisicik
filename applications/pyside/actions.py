# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DQT_PHONON_INCLUDE_DIR=/usr/include/phonon \
                          -DQT_QMAKE_EXECUTABLE=/usr/bin/qmake \
                          -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                          -DPYTHON_SUFFIX=-python2.7 \
                          -DQT_SRC_DIR=/usr/lib \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir="..")

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
