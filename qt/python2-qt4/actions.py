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

WorkDir="PyQt-x11-gpl-%s" % get.srcVERSION()

def setup():
    #pisitools.dosed("configure.py", "  check_license()", "# check_license()")
    #pythonmodules.run("configure.py -q /usr/bin/qmake-qt4")
    pythonmodules.run("configure.py --confirm-license \
                                    --qsci-api \
                                    --destdir='/usr/lib/python2.7/site-packages' \
                                    --qmake='/usr/bin/qmake-qt4' ")
    shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")
  
def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("NEWS", "README", "THANKS", "LICENSE*", "GPL*", "OPENSOURCE*")
