#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    #pisitools.dosed("configure", "gdk-pixbuf-query-loaders-[2346]+\s", "")
    #if get.buildTYPE() == "emul32":
        #pisitools.dosed("configure", "(gdk-pixbuf-query-loaders)([\s\]])", r"\1-32\2")

    autotools.autoreconf("-vif")
    autotools.configure("--disable-gtk-doc \
                         --enable-pixbuf-loader=yes \
                         --disable-static \
                         --enable-vala \
                         --with-gtk2 \
                         --enable-introspection ")

    #pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    #pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    #pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog", "README")
