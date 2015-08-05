#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --disable-static \
                         --disable-debug \
                         --enable-release \
                         --libexecdir=/usr/lib \
                         PYTHON=/usr/bin/python")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/usr/share/gconf/schemas")
    pisitools.domove("/etc/gconf/schemas/awn.schemas", "/usr/share/gconf/schemas")
    pisitools.removedir("/etc")
    pisitools.dodoc("AUTHORS", "COPYING")