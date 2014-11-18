#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("sed -i -e 's:getgroups:lightdm_&:' tests/src/libsystem.c")
    autotools.configure("--enable-introspection \
                         --enable-liblightdm-gobject \
                         --libexecdir=/usr/lib/lightdm \
                         --with-greeter-user=lightdm \
                         --with-greeter-session=lightdm-gtk-greeter \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.remove("/etc/init")
    #pisitools.removeDir("/usr/include/lightdm-qt-3")
    #pisitools.dodir("/var/cache/lightdm")
    #pisitools.dodir("/var/lib/lightdm")
    #pisitools.dodir("/var/log/lightdm")
    pisitools.dodir("/usr/lib/systemd/system/graphical.target.wants")
    pisitools.dosym("/usr/lib/systemd/system/lightdm.service", "/usr/lib/systemd/system/displaymanager.service")
    pisitools.dosym("/usr/lib/systemd/system/lightdm.service", "/usr/lib/systemd/system/graphical.target.wants/lightdm.service")
