#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import qt4
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("qmake qtLogout.pro")

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.domove("usr/local/bin/qtLogout", "usr/bin/", "qlogout")
    pisitools.removeDir("usr/local")

