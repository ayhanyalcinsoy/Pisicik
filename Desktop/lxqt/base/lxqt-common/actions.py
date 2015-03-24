#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/=/usr/share/cmake", "/usr/share")
    pisitools.removeDir("/usr/=/")
    pisitools.remove("/usr/share/desktop-directories/*.directory")
    #pisitools.remove("/etc/lxqt/*.conf")
    #pisitools.remove("etc/pcmanfm-qt/lxqt/*.conf")

    pisitools.remove("/usr/share/lxqt/themes/Ambiance/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/Dark/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/Frost/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/Kde-plasma/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/Light/mainmenu.svg")

    pisitools.remove("/usr/share/lxqt/themes/Dark/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/Dark/lxqt-panel.qss")
    pisitools.remove("/usr/share/lxqt/themes/Frost/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/Kde-plasma/wallpaper.cfg")
    shelltools.cd("..")
    pisitools.dodoc("README.md")