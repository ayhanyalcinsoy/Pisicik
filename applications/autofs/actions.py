#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("samples/auto.master", "/etc/auto.misc", "/etc/autofs/auto.misc")
    #pisitools.dosed("samples/auto.master", "/etc/auto.master.d", "/etc/autofs/auto.master.d")
    autotools.autoreconf("-vif")
    autotools.configure("--enable-ignore-busy \
                         --without-systemd \
                         --without-hesiod \
                         --sbindir=/usr/bin \
                         --with-mapdir=/etc/autofs \
                         --with-libtirpc")

#--disable-mount-move --disable-mount-locking --with-sasl=yes --with-fifodir=/run/autofs 

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALLROOT=%s" % get.installDIR())

    #pisitools.removeDir("/etc/init.d")

    pisitools.dodoc("CREDITS", "COPY*", "samples/ldap*", "samples/autofs.schema")
