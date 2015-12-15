#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qt-creator-opensource-src-%s" % get.srcVERSION()

def setup():
    shelltools.system("LLVM_INSTALL_DIR=/%s qmake-qt5 -r qtcreator.pro" % get.installDIR())
    #qt5.configure("LLVM_INSTALL_DIR=/usr")

def build():
    qt5.make()

def install():
    #pisitools.dodir("/usr")
    qt5.install()
    #pisitools.domove("/share", "/usr")
   # pisitools.domove("/lib", "/usr")
    #pisitools.domove("/bin", "/usr")
    #pisitools.rename("/usr/bin/qtcreator", "qtcreator-bin")
   # pisitools.domove("/usr/share/qtcreator/debugger/LGPL_EXCEPTION.TXT", "/usr/share/licenses/qtcreator")
