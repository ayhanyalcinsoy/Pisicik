#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

#WorkDir = 'pds-%s' % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.domove("/usr/lib/python2.7/site-packages", "/usr/lib/python3.4")
    pisitools.removeDir("/usr/lib/python2.7")
