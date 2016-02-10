#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure("--sysconfdir=/etc --localstatedir=/var \
              --disable-static --enable-eudev \
              --with-eudev-rulesdir=/usr/lib/eudev/rules.d \
              --with-usb-ids-path=/usr/share/hwdata/usb.ids \
              --with-pci-ids-path=/usr/share/hwdata/pci.ids")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING")