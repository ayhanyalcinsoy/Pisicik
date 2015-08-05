#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    #shelltools.system("svn up")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_HTTP_STREAM_PLAYBACK=ON \
                          -DENABLE_KDE=OFF -DENABLE_QT5=ON \
                          -DENABLE_UDISKS2=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "LICENSE", "ChangeLog", "TODO", "INSTALL", "README")

    pisitools.insinto("/usr/share/pixmaps/", "streams/icons/stream.png", "cantata.png")