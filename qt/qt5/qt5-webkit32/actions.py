#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
    shelltools.export("QT5LINK", "/usr/lib/qt5/bin")
    #shelltools.system ("qmake-qt5 WebKit.pro -config  -no-use-gold-linker")
    if not get.buildTYPE() == "emul32":
        qt5.configure()

    else:
       shelltools.system("qmake-qt5 QMAKE_CXXFLAGS+=-Wno-c++0x-compat WebKit.pro")
       shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    qt5.make()
    # Fix docs build when qt is not installed
    #shelltools.system('sed -i "s|/usr/lib/qt/bin/qhelpgenerator|${QTDIR}/qttools/bin/qhelpgenerator|g" Source/Makefile.api')
    #shelltools.system("find -name Makefile -exec sed -i 's|/usr/lib/qt/bin/qmlplugindump|${QTDIR}/qtdeclarative/bin/qmlplugindump|g' {} +")

def install():
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/bin")
    if get.buildTYPE() == "emul32":
        qt5.install("INSTALL_ROOT=%s32" % get.installDIR())
        shelltools.move("%s32/usr/lib32" % get.installDIR(), "%s/usr" % get.installDIR())
        return
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #pisitools.insinto("/usr/share/licenses/qt5-webkit/", "LGPL_EXCEPTION.txt")
