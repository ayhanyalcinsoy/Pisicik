# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
		          -DCMAKE_BUILD_TYPE=Release \
		          -DBUILD_DESIGNER_PLUGIN=0 \
		          -DUSE_QT5=true")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/lib64/*", "usr/lib/")
    pisitools.removeDir("/usr/lib64")
#    pisitools.dobin("src/test")
#    pisitools.rename("/usr/bin/test", "consoleq")

    #pisitools.remove("/usr/include/qtermwidget4/qtermwidget.h")
    #pisitools.insinto("/usr/include/qtermwidget4", "lib/*.h")
    #pisitools.insinto("/usr/lib/pkgconfig", "qtermwidget4.pc")

    pisitools.dodoc("AUTHORS", "README", "COPYING")