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

WorkDir="."

def install():
    pisitools.insinto("/usr/bin","qtfind-1.2/usr/bin/qtfind")
    pisitools.insinto("/usr/lib","qtfind-1.2/usr/lib/qtfind_i18n")
    pisitools.insinto("/usr/share/file-manager","qtfind-1.2/usr/share/file-manager/actions")
    pisitools.insinto("/usr/share","qtfind-1.2/usr/share/pixmaps")