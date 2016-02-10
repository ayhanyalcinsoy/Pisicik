#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

#def setup():
    #shelltools.export("oopath", "/usr/lib/libreoffice/program")
    #shelltools.export("ooure", "/usr/lib/libreoffice/program")
    #shelltools.export("oobasis", "/usr/lib/libreoffice/program")
    
    
def build():
    #shelltools.cd("Setup")
    pisitools.dosed("Setup/Makefile", "DESTDIR=/usr/local", "DESTDIR=/usr")
    pisitools.dosed("Setup/Makefile", "oopath=/usr/lib/openoffice/program", "oopath=/usr/lib/libreoffice/program")
    pisitools.dosed("Setup/Makefile", "ooure=/usr/lib/openoffice/program", "ooure=/usr/lib/libreoffice/program")
    pisitools.dosed("Setup/Makefile", "oobasis=/usr/lib/openoffice/program", "oobasis=/usr/lib/libreoffice/program")
    autotools.make("-f Setup/Makefile DESTDIR=/usr python=/usr/bin/python")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodir("/usr")
    #pisitools.domove("/share", "/usr")
    #pisitools.domove("/bin", "/usr")
    #pisitools.dosym("/usr/share/bibus/bibusStart.py", "/usr/bin/bibus")
    #pisitools.remove("/usr/share/bibus/Setup/uninstall.sh")