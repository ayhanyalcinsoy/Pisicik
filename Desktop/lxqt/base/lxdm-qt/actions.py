#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #install Pisi Linux default theme
    pisitools.insinto("/usr/share/lxdm/themes", "lxdm-pisilinux-theme")
    pisitools.domove("/usr/share/lxdm/themes/lxdm-pisilinux-theme/*.*" , "/usr/share/lxdm/themes/pisilinux")
    pisitools.domove("/usr/share/lxdm/themes/lxdm-pisilinux-theme/gtkrc" , "/usr/share/lxdm/themes/pisilinux")
    pisitools.removeDir("/usr/share/lxdm/themes/lxdm-pisilinux-theme")
    pisitools.removeDir("/usr/share/lxdm/themes/Industrial")
    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "README", "ChangeLog", "NEWS")
