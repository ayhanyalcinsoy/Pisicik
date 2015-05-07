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
    #shelltools.system("qmake-qt5 WebKit.pro")
    qt5.configure()
     
def build():
    qt5.make()

def install():
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/bin")
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)
           
    pisitools.dodoc("LICENSE.GPLv2", "LICENSE.LGPLv3", "LICENSE.LGPLv21", "ChangeLog-2012-05-22")
