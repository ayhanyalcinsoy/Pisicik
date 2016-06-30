#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-default-backend=pisi \
                         --enable-pisi \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-ruck \
                         --disable-dummy \
                         --disable-systemd \
                         --libexecdir=/usr/lib \
                         --disable-browser-plugin ")
                         #--with-dbus-services=/usr/share/dbus-1/system-services \
                         #--with-dbus-sys=/etc/dbus-1 \
                         #--with-security-framework=polkit \
                         #--disable-tests \

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.insinto("/etc/dbus-1/system.d","data/org.freedesktop.PackageKit.conf")
    pisitools.dodoc("README", "MAINTAINERS", "HACKING", "AUTHORS", "NEWS")
