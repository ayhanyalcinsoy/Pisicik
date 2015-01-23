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

def setup():
    autotools.rawConfigure ("-opensource \
                             -eglfs \
                             -opengl es2 \
                             -xcb \
                             -no-pch \
                             -dbus-linked \
                             -icu \
                             -cups \
                             -nis \
                             -widgets \
                             -gui \
                             -qt-xcb \
                             -openssl-linked \
                             -system-libjpeg \
                             -system-libpng \
                             -system-zlib \
                             -largefile \
                             -c++11 \
                             -shared \
                             -no-static \
                             -confirm-license \
                             -release \
                             -prefix /usr \
                             -archdatadir /usr/lib/qt5 \
                             -datadir /usr/share/qt5 \
                             -docdir /usr/share/doc/qt5 \
                             -sysconfdir /etc/xdg \
                             -nomake tests \
                             -examplesdir /usr/lib/qt5/examples")
def build():
    autotools.make ()

def install():
    autotools.rawInstall ("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.insinto("/usr/share/licenses/qt5-x11extras/", "LGPL_EXCEPTION.txt")
