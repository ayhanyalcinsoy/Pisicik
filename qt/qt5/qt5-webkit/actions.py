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
    shelltools.system("qmake-qt5 WebKit.pro -config --no-webkit1 ")

def build():
    qt5.make()

def install():
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    #shelltools.system("find -type f -name -print0 | grep -FzZ “/usr/lib/*.prl -exec” sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {} \;")

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    #pisitools.insinto("/usr/share/licenses/qt5-webkit/", "LGPL_EXCEPTION.txt")
