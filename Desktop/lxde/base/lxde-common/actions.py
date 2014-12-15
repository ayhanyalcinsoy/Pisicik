#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/etc/xdg")
    pisitools.remove("/usr/share/applications/lxde-screenlock.desktop")
    pisitools.remove("/usr/share/applications/lxde-logout.desktop")
    pisitools.remove("/usr/share/lxde/images/logout-banner.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

