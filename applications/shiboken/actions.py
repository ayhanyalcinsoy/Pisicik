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

WorkDir = ".."

def setup():
    shelltools.cd(".")
    shelltools.makedirs("build_python3")
    shelltools.copytree("work/shiboken-1.2.2/", "build_python3")
    #python2
    shelltools.cd("work/shiboken-1.2.2/")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
                          -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir="..")

    #python3
    shelltools.cd(".../build_python3/")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
                          -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                          -DUSE_PYTHON3=yes \
                          -DBUILD_TESTS=OFF \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir="..")

def build():
    #python2
    shelltools.cd("work/shiboken-1.2.2/")
    autotools.make()
    #python3
    shelltools.cd("build2")
    autotools.make()
def install():
    #Python2
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #Python3
    shelltools.cd("build2")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("usr/bin")
    pisitools.removeDir("usr/include")
    pisitools.removeDir("usr/share")
    pisitools.remove("usr/lib/cmake/Shiboken-1.2.2/ShibokenConfigVersion.cmake")
    pisitools.remove("usr/lib/cmake/Shiboken-1.2.2/ShibokenConfig.cmake")
