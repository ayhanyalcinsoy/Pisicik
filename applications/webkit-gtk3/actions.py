#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("CFLAGS", "%s -I/usr/include/glib-2.0" % get.CFLAGS())
shelltools.export("CFLAGS", "%s -I/usr/lib/glib-2.0/include/" % get.CFLAGS())

shelltools.export("XDG_DATA_HOME", get.workDIR())
pisitools.flags.replace("-ggdb3", "-g")

#paths = ["JavaScriptCore", "WebCore", "WebKit"]
docs = ["AUTHORS", "ChangeLog", "COPYING.LIB", "THANKS", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    autotools.autoreconf ("-v")
    autotools.configure("--disable-gtk-doc \
                         --disable-webkit2 \
                         --enable-introspection \
                         --with-gtk=3.0 \
                         --prefix=/usr \
                         --libexecdir=/usr/lib/webkit-2.4.8")

    pisitools.dosed("libtool", " -shared ", "-Wl,-O1,--as-needed\0/g")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/gtk-doc/html", "/usr/share/doc/webkit-gtk3")

    pisitools.dodoc("NEWS")
    shelltools.cd("Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                pisitools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))
