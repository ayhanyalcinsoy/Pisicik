#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

import os

WorkDir = "qtbase-opensource-src-5.4.0"
#% get.srcVERSION().replace('_','-').replace('pre1', 'tp')

qtbase = qt5.prefix
#absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

#Temporary bindir to avoid qt4 conflicts
bindirQt5="/usr/lib/qt5/bin"


#shelltools.export("CFLAGS", filteredCFLAGS)
#shelltools.export("CXXFLAGS", filteredCXXFLAGS)
#check that dosed commands without releated patches
#pisitools.dosed("mkspecs/common/gcc-base-unix.conf", "\-Wl,\-rpath,")
#pisitools.dosed("mkspecs/common/gcc-base.conf", "\-O2", filteredCFLAGS)
#pisitools.dosed("mkspecs/common/gcc-base.conf", "^(QMAKE_LFLAGS\s+\+=)", r"\1 %s" % get.LDFLAGS())

def setup():
    #shelltools.system('sed -i -e "s|^\(QMAKE_CFLAGS_RELEASE.*\)|\1 ${CFLAGS}|" ./mkspecs/common/gcc-base.conf')
    #shelltools.system('sed -i -e "s|^\(QMAKE_LFLAGS_RELEASE.*\)|\1 ${LDFLAGS}|" ./mkspecs/common/g++-unix.conf')
    #make sure we don't use them
    for d in ('libjpeg', 'freetype', 'libpng', 'zlib'):
        shelltools.unlinkDir("src/3rdparty/%s" % d)

    """filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PISILINUX_CC" :       get.CC(),
            "PISILINUX_CXX":       get.CXX(),
            "PISILINUX_CFLAGS":    filteredCFLAGS,
            "PISILINUX_LDFLAGS":   get.LDFLAGS()}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++-base.conf", k, v)
        pisitools.dosed("mkspecs/common/g++-unix.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)"""

    #-no-pch makes build ccache-friendly
    autotools.rawConfigure("-v \
                   -no-pch \
                   -confirm-license \
                   -opensource \
                   -optimized-qmake \
                   -nomake tests \
                   -no-rpath \
                   -release \
                   -shared \
                   -accessibility \
                   -dbus-linked \
                   -fontconfig \
                   -glib \
                   -gtkstyle \
                   -icu \
                   -c++11 \
                   -system-harfbuzz \
                   -openssl-linked \
                   -system-libjpeg \
                   -system-libpng \
                   -system-sqlite \
                   -system-zlib \
                   -plugin-sql-sqlite \
                   -plugin-sql-odbc \
                   -plugin-sql-psql \
                   -plugin-sql-ibase \
                   -no-sql-tds \
                   -I/usr/include/firebird/ \
                   -I/usr/include/postgresql/server/ \
                   -no-separate-debug-info \
                   -no-strip \
                   -prefix %s \
                   -bindir %s \
                   -archdatadir %s\
                   -libdir %s \
                   -docdir %s \
                   -examplesdir %s \
                   -plugindir %s \
                   -translationdir %s \
                   -sysconfdir %s \
                   -datadir %s \
                   -importdir %s \
                   -headerdir %s \
                   -reduce-relocations" % (qt5.prefix, bindirQt5, qt5.archdatadir, qt5.libdir, qt5.docdir, qt5.examplesdir, qt5.plugindir, qt5.translationdir, qt5.sysconfdir, qt5.datadir, qt5.importdir, qt5.headerdir))

def build():
    #shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    autotools.make()

def install():
    pisitools.dodir(qt5.libdir)
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    #for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
    #    pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    # We should work on Turkish translations :)
    shelltools.export("LD_LIBRARY_PATH", "%s%s" % (get.installDIR(), qt5.libdir))
    #shelltools.system("%s%s/lrelease l10n-tr/*.ts" % (get.installDIR(), bindirQt5))
    #pisitools.insinto(qt5.translationdir, "l10n-tr/*.qm")

    #Fix all occurances of WorkDir in pc files
    #pisitools.dosed("%s%s/pkgconfig/*.pc" % (get.installDIR(), qt5.libdir), "%s/qt-x11-opensource-src-%s" % (get.workDIR(), get.srcVERSION()), qt5.prefix)

    #mkspecPath = "%s ./mkspecs" %  qt5.archdatadir
    mkspecPath = "/usr/share/qt5/mkspecs"

    for root, dirs, files in os.walk("%s/usr" % get.installDIR()):
        # Remove unnecessary spec files..
        if root.endswith(mkspecPath):
            for dir in dirs:
                if not dir.startswith("linux") and dir not in ["common","qws","features","default"]:
                    pisitools.removeDir(os.path.join(mkspecPath,dir))
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name), "^QMAKE_PRL_BUILD_DIR.*", "")

    pisitools.dodoc("LGPL_EXCEPTION.txt", "LICENSE.*")
