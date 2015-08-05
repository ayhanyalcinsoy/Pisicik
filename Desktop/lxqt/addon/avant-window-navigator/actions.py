#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --disable-static \
                         PYTHON=/usr/bin/python")

def build():
    autotools.make("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/usr/share/gconf/schemas")
    pisitools.domove("/etc/gconf/schemas/awn.schemas", "/usr/share/gconf/schemas")
    pisitools.removedir("/etc")
    pisitools.dodoc("AUTHORS", "COPYING")