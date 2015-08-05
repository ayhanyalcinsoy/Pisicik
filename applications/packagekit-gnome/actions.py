#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.sym("/bin/true", "%s/py-compile" % get.curDIR())
    autotools.configure("--prefix=/usr \
		--sysconfdir=/etc \
		--disable-schemas-compile \
		--disable-gtk-doc \
                PYTHON=/usr/bin/python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "TODO", "MAINTAINERS", "AUTHORS", "NEWS")

