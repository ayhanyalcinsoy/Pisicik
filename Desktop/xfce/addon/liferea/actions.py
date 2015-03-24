#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --enable-libnotify \
                         --localstatedir=/var \
                         --disable-schemas-compile\
                         --disable-silent-rules")

    #pisitools.dosed("libtool"," -shared ", "-Wl, -01 --as-needed -shared ")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Empty files: NEWS
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
