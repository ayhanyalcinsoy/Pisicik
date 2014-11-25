#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def install():
    pythonmodules.install()
    #flat-dark-alpha
    pisitools.insinto("/usr/share/lxqt/themes/flat-dark-alpha/" , "/usr/share/lxqt/themes/flat-dark-alpha/amego.png")
    pisitools.insinto("/usr/share/lxqt/themes/flat-dark-alpha/" , "/usr/share/lxqt/themes/flat-dark-alpha/mainmenu.svg")
    pisitools.insinto("/usr/share/lxqt/themes/flat-dark-alpha/" , "/usr/share/lxqt/themes/flat-dark-alpha/wallpaper.cfg")