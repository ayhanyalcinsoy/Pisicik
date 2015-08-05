#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.compile()
    pythonmodules.install()
    pisitools.dodir("/usr/share/avant-window-navigator/applets")
    pisitools.insinto("/usr/share/avant-window-navigator/applets", "AWN/*")

