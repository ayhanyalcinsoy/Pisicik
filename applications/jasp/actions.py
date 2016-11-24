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
    shelltools.system("qmake-qt5 R_HOME=/usr/lib/R PREFIX=/usr JASP.pro")

def build():
    qt5.make()

def install():
    #qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    #Install files
    pisitools.dodir("/usr/share/jasp")
    pisitools.insinto("/usr/share/jasp","R")
    pisitools.insinto("/usr/share/jasp", "jasp")
    pisitools.insinto("/usr/share/jasp", "JASPEngine")
    pisitools.insinto("/usr/share/jasp","Resources")
    pisitools.insinto("/usr/share/jasp","libJASP-Common.a")
    
    #Install icon
    pisitools.dodir("/usr/share/pixmaps")
    pisitools.insinto("/usr/share/jasp/Resources", "/Tools/debian/jasp.svg")
    
    #Install .desktop file
    pisitools.dodir("/usr/share/applications")
    pisitools.insinto("/usr/share/applications", "/Tools/debian/jasp.desktop")

    #Install link to binary
    pisitools.dodir("/usr/bin")
    pisitools.dosym("/usr/share/jasp/jasp", "/usr/bin/JASP")
    
    pisitools.dodoc("LGPL_EXCEPTION.txt")
