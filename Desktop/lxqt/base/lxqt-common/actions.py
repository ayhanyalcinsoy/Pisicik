#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib\
                          -DUSE_QT5=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/etc/lxqt/*.conf")
    pisitools.remove("etc/pcmanfm-qt/lxqt/*.conf")

    pisitools.remove("/usr/share/lxqt/themes/ambiance/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/dark/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/frost/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/kde-plasma/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/light/mainmenu.svg")

    pisitools.remove("/usr/share/lxqt/themes/ambiance/*.jpg")

    pisitools.remove("/usr/share/lxqt/themes/ambiance/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/dark/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/frost/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/kde-plasma/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/light/wallpaper.cfg")

    pisitools.dodoc("README.md")