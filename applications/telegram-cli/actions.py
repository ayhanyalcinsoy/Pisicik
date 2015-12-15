#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-libconfig \
                         --enable-liblua \
                         --with-progname=telegram-cli \
                         --with-openssl=/usr \
                         --with-zlib=/usr/lib \
                         --disable-json \
                         --enable-extf \
                         --disable-valgrind ")

def build():
    autotools.make()

def install():
     autotools.rawInstall("DESTDIR=%s" % get.installDIR())
     pisitools.insinto("/etc/telegram-cli/" , "/etc/telegram-cli/server.pub")
     pisitools.insinto("/usr/bin/" , "/bin/telegram-cli")

# By PiSiDo 2.3.1
