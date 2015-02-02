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

import os

WorkDir = "qtbase-opensource-src-5.4.0"

qtbase = qt5.prefix


#Temporary bindir to avoid qt4 conflicts
bindirQt5="/usr/lib/qt5/bin"

def setup():
    autotools.rawConfigure("-no-pch \
                     -confirm-license \
                     -opensource \
                     -optimized-qmake \
                     -nomake tests \
                     -no-rpath \
                     -release \
                     -shared \
                     -accessibility \
                     -dbus-linked \
                     -fontconfig \
                     -glib \
                     -gtkstyle \
                     -icu \
                     -c++11 \
                     -system-harfbuzz \
                     -openssl-linked \
                     -system-libjpeg \
                     -system-libpng \
                     -system-sqlite \
                     -system-zlib \
                     -plugin-sql-sqlite \
                     -plugin-sql-odbc \
                     -plugin-sql-psql \
                     -plugin-sql-ibase \
                     -plugin-sql-mysql \
                     -no-sql-tds \
                     -openssl-linked \
                     -prefix /usr \
                     -bindir /usr/lib/qt5/bin \
                     -docdir /usr/share/doc/qt5 \
                     -headerdir /usr/include/qt \
                     -archdatadir /usr/lib/qt5 \
                     -datadir /usr/share/qt5 \
                     -sysconfdir /etc/xdg \
                     -examplesdir /usr/share/doc/qt5/examples")

def build():
     autotools.make()

def install():
    pisitools.dodir(qt5.libdir)
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #mkspecPath = "%s ./mkspecs" %  qt5.archdatadir
    mkspecPath = "/usr/share/qt5/mkspecs"

    pisitools.dodoc("LGPL_EXCEPTION.txt", "LICENSE.*")
