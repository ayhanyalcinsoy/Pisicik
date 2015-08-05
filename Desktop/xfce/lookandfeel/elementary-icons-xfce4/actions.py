#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = 'elementary-icons-xfce4-%s' % get.srcVERSION()

#def setup():
    #autotools.configure()

#def build():
    #autotools.make()

def install():
    pisitools.insinto("/usr/share/icons", "elementary-xfce")
    pisitools.insinto("/usr/share/icons", "elementary-xfce-dark")
    pisitools.insinto("/usr/share/icons", "elementary-xfce-darker")
    pisitools.insinto("/usr/share/icons", "elementary-xfce-darkest")
    pisitools.dodoc("elementary-xfce/AUTHORS", "elementary-xfce/LICENSE", "elementary-xfce/CONTRIBUTORS")
