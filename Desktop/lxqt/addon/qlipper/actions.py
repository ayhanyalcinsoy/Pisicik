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
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DUSE_SYSTEM_QTSA=0 \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DQT_QMAKE_EXECUTABLE=qmake", sourceDir=".")

def build():
    autotools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
