#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="PyQt-gpl-%s" % get.srcVERSION()

def setup():
    pythonmodules.run("configure.py --confirm-license \
                                    --qsci-api \
                                    --sip /usr/bin/sip \
                                    --qmake='/usr/bin/qmake-qt5' \
                                    --destdir='/usr/lib/python3.4/site-packages' \
                                    --sip-incdir='/usr/include/python3.4m' \
                                    CFLAGS='%s' CXXFLAGS='%s'" % (get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")
    shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")
    
def build():
    autotools.make()

def install():    
    shelltools.cd("%s/PyQt-gpl-5.5" % get.workDIR())
    autotools.rawInstall("-C pyrcc DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("-C pylupdate DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    #pisitools.insinto("/usr/share/sip/PyQt5", "./sip/*")
     # Fix conflicts with python-pyqt5
    #pisitools.rename("/usr/bin/pyuic5", "python3-pyuic5")

    
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("NEWS", "README","LICENSE*")
