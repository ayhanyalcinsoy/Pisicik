#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("qmake-qt5 qtLogout.pro")

def build():
    qt5.make()

def install():
    qt5.install()
    mkspecPath = "/usr/share/qt5/mkspecs"
    pisitools.domove("usr/local/bin/qtLogout", "usr/bin/", "qlogout")
    pisitools.removeDir("usr/local")
