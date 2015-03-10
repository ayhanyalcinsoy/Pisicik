#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.configure("python2 waf configure --prefix=/usr")
    pythonmodules.build("python2 waf build")

def install():
    pythonmodules.install("walf")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

