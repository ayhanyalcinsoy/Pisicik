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

WorkDir = "qtbase-opensource-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')

qtbase = qt5.prefix
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

#Temporary bindir to avoid qt4 conflicts
bindirQt5="/usr/lib/qt5/bin"

def setup():
    #shelltools.system('sed -i -e "s|^\(QMAKE_CFLAGS_RELEASE.*\)|\1 ${CFLAGS}|" mkspecs/common/gcc-base.conf')
    #shelltools.system('sed -i -e "s|^\(QMAKE_LFLAGS_RELEASE.*\)|\1 ${LDFLAGS}|" mkspecs/common/g++-unix.conf')

    checkdeletepath="%s/qtbase/src/3rdparty"  % absoluteWorkDir
    for dir in ('libjpeg', 'freetype', 'libpng', 'zlib', "xcb", "sqlite"):
        if os.path.exists(checkdeletepath+dir):
            shelltools.unlinkDir(checkdeletepath+dir)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PISILINUX_CC" :       get.CC() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CXX":       get.CXX() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CFLAGS":    filteredCFLAGS + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_LDFLAGS":   get.LDFLAGS() + (" -m32" if get.buildTYPE() == "emul32" else "")}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++-base.conf", k, v)
        pisitools.dosed("mkspecs/common/g++-unix.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    #check that dosed commands without releated patches
    pisitools.dosed("mkspecs/common/gcc-base-unix.conf", "\-Wl,\-rpath,")
    pisitools.dosed("mkspecs/common/gcc-base.conf", "\-O2", filteredCFLAGS)
    pisitools.dosed("mkspecs/common/gcc-base.conf", "^(QMAKE_LFLAGS\s+\+=)", r"\1 %s" % get.LDFLAGS())

    if not get.buildTYPE() == "emul32":
        #-no-pch makes build ccache-friendly
        options = "-v \
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
                   -reduce-relocations" % (qt5.prefix, bindirQt5, qt5.archdatadir, qt5.libdir, qt5.docdir, qt5.examplesdir, qt5.plugindir, qt5.translationdir, qt5.sysconfdir, qt5.datadir, qt5.importdir, qt5.headerdir)
    else:
        pisitools.dosed("mkspecs/linux-g++-64/qmake.conf", "-m64", "-m32")
        shelltools.export("LDFLAGS", "-m32 %s" % get.LDFLAGS())
        options = "-no-pch \
                   -v \
                   -platform linux-g++-32 \
                   -prefix /usr \
                   -libdir /usr/lib32 \
                   -plugindir /usr/lib32/qt5/plugins \
                   -importdir /usr/lib32/qt5/imports \
                   -datadir /usr/share/qt5 \
                   -translationdir /usr/share/qt5/translations \
                   -sysconfdir /etc \
                   -qt-zlib \
                   -qt-libjpeg \
                   -qt-libpng \
                   -qt-xcb \
                   -qt-xkbcommon \
                   -qt-freetype \
                   -qt-pcre \
                   -qt-harfbuzz \
                   -nomake tests \
                   -openssl-linked \
                   -nomake examples \
                   -nomake tools \
                   -optimized-qmake \
                   -no-rpath \
                   -no-strip \
                   -dbus-linked \
                   -no-openvg \
                   -no-sse2 \
                   -confirm-license \
                   -reduce-relocations  \
                   -no-use-gold-linker \
                   -opensource "

    autotools.rawConfigure(options)

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    autotools.make()
    # Fix docs build when qt is not installed
    shelltools.system('sed -i "s|/usr/lib/qt/bin/qdoc|${QTDIR}/qtbase/bin/qdoc|g" qmake/Makefile.qmake-docs')
    #shelltools.system("find -name Makefile -exec sed -i "s|/usr/lib/qt/bin/qdoc|${QTDIR}/qtbase/bin/qdoc|g" {} +")
    shelltools.system('sed -i "s|/usr/lib/qt/bin/qhelpgenerator|${QTDIR}/qttools/bin/qhelpgenerator|g" qmake/Makefile.qmake-docs')
    #shelltools.system("find -name Makefile -exec sed -i "s|/usr/lib/qt/bin/qhelpgenerator|${QTDIR}/qttools/bin/qhelpgenerator|g" {} +")

def install():
    if get.buildTYPE() == "emul32":
        qt5.install("INSTALL_ROOT=%s32" % get.installDIR())
        shelltools.move("%s32/usr/lib32" % get.installDIR(), "%s/usr" % get.installDIR())
        return

    pisitools.dodir(qt5.libdir)
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    # Drop QMAKE_PRL_BUILD_DIR because reference the build dir
    #shelltools.system("find /usr/lib -type f -name '*.prl -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {}")

    # Fix wrong qmake path in pri file
    #shelltools.system('sed -i "s|${srcdir}/${_pkgfqn}/qtbase|/usr|" /usr/lib/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri')

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    mkspecPath = "%s/mkspecs" %  qt5.archdatadir

    for root, dirs, files in os.walk("%s%s" % (get.installDIR(),  qt5.archdatadir)):
        # Remove unnecessary spec files..
        if root.endswith(mkspecPath):
            for dir in dirs:
                if not dir.startswith("linux") and dir not in ["common","qws","features","default"]:
                    pisitools.removeDir(os.path.join(mkspecPath,dir))
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name), "^QMAKE_PRL_BUILD_DIR.*", "")

    pisitools.dodoc("LGPL_EXCEPTION.txt", "LICENSE.*")
