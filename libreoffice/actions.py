#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os
import psutil
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

pisitools.ldflags.add("-L/usr/lib/nss")
pisitools.flags.remove("-pipe", "-Wall", "-g", "-fexceptions")
shelltools.export("ARCH_FLAGS", get.CXXFLAGS())
shelltools.export("LINKFLAGSOPTIMIZE", get.LDFLAGS())
shelltools.export("PYTHON", get.curPYTHON())
shelltools.export("LC_ALL", "C")

langpackdir = "%s-langpack-%s" % (get.srcNAME(), get.srcVERSION())
langpackpath = os.path.normpath("%s/../%s" % (get.installDIR(), langpackdir))
langs = "en-US af ar as bg bn br ca cs cy da de dz el es et eu fa fi fr ga gl gu he hr hu it ja ko kn lt lv mai ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-CN zh-TW zu"
ldirs = ("/usr/lib/libreoffice/help/%s",
         "/usr/lib/libreoffice/share/autotext/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/cui/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/sfx/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/svt/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/svx/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/vcl/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/desktop/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/scalc/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/sdraw/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/smath/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/simpress/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/swriter/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/modules/BasicIDE/ui/res/%s",
         "/usr/lib/libreoffice/share/config/soffice.cfg/filter/ui/res/%s",
         "/usr/lib/libreoffice/share/extensions/nlpsolver/help/%s",
         "/usr/lib/libreoffice/share/extensions/wiki-publisher/help/%s")

def setup():
    vars = {"lang": langs,
            "jobs": psutil.NUM_CPUS,
            "etar": get.workDIR()}

    shelltools.system("ulimit -c unlimited")
    autotools.aclocal("-I m4")
    autotools.autoconf()
    # avoid running autogen.sh on make
    shelltools.touch("autogen.lastrun")
    autotools.rawConfigure('--with-vendor="PisiLinux" \
                       --with-ant-home="/usr/share/ant" \
                       --prefix=/usr --exec-prefix=/usr --sysconfdir=/etc \
                       --libdir=/usr/lib --mandir=/usr/share/man \
                       --enable-release-build \
                       --disable-verbose \
                       --disable-dependency-tracking \
                       --enable-crashdump \
                       --with-system-libs \
                       --with-system-headers \
                       --with-lang="%(lang)s" \
                       --enable-dbus \
                       --enable-evolution2 \
                       --enable-gio \
                       --disable-gnome-vfs \
                       --disable-kde \
                       --enable-kde4 \
                       --enable-lockdown \
                       --enable-opengl \
                       --enable-odk \
                       --enable-scripting-beanshell \
                       --enable-scripting-javascript \
                       --enable-ext-wiki-publisher \
                       --enable-ext-nlpsolver \
                       --enable-python=system \
                       --without-system-icu \
                       --with-system-cairo \
                       --with-system-mythes \
                       --with-system-libcdr \
                       --with-system-libwpg \
                       --with-system-libwps \
                       --with-system-redland \
                       --with-system-clucene \
                       --with-system-libmspub \
                       --with-system-cppunit \
                       --with-system-mdds \
                       --with-system-libodfgen \
                       --with-system-libetonyek \
                       --with-system-libatomic_ops \
                       --enable-split-app-modules \
                       --enable-avahi \
                       --enable-gtk3 \
                       --enable-gstreamer \
                       --disable-gstreamer-0-10 \
                       --enable-opencl \
                       --enable-openssl \
                       --enable-orcus \
                       --disable-telepathy \
                       --without-ppds --without-afms --without-fonts --without-system-apache-commons --without-system-libcmis \
                       --without-system-libexttextcat --without-system-jfreereport \
                       --with-system-libvisio \
                       --with-helppack-integration \
                       --with-system-beanshell \
                       --with-system-graphite \
                       --with-system-dicts \
                       --without-system-liblangtag --without-system-harfbuzz --without-system-boost --without-system-orcus \
                       --without-system-hsqldb --without-system-libmwaw \
                       --without-system-libfreehand --without-system-libebook --without-system-firebird --without-system-libabw \
                       --without-myspell-dicts --without-system-npapi-headers \
                       --with-external-dict-dir=/usr/share/hunspell \
                       --with-external-hyph-dir=/usr/share/hyphen \
                       --with-external-thes-dir=/usr/share/mythes \
                       --with-alloc=system \
                       --disable-fetch-external \
                       --with-parallelism=%(jobs)s \
                       --with-external-tar="%(etar)s"' % vars)

def build():
    autotools.make()
    pisitools.dosed("workdir/CustomTarget/sysui/share/oxygenoffice/startcenter.desktop", "GenericName\[tr\]=Ofis", "GenericName[tr]=Ofis Uygulamaları")

def check():
    autotools.make("unitcheck")
    autotools.make("slowcheck")

def install():
    autotools.rawInstall("DESTDIR=%s distro-pack-install -o build -o check" % get.installDIR())

    #kill rpath bombs, strip unstripped shared libararies
    shelltools.system("strip --strip-unneeded %s/usr/lib/libreoffice/program/librdf-lo.so.0" % get.installDIR())
    shelltools.system("strip --strip-unneeded %s/usr/lib/libreoffice/program/librasqal-lo.so.3" % get.installDIR())   
    pisitools.dosed("/usr/lib/libreoffice/share/xdg/math.desktop", "Categories=Office;Education;Science;Math;X-Red-Hat-Base;X-MandrivaLinux-Office-Other;", "Categories=Office;")
    pisitools.dosed("/usr/lib/libreoffice/share/xdg/draw.desktop", "Categories=Office;Education;Science;Math;X-Red-Hat-Base;X-MandrivaLinux-Office-Other;", "Categories=Office;")

    if not shelltools.isDirectory(langpackpath): shelltools.makedirs(langpackpath)
    else: shelltools.unlinkDir(langpackpath)
    for l in langs.split(" "):
        if l == "en-US": continue
        print("processing: %s" % l)
        for ld in ldirs:
            srcd = "%s%s" % (get.installDIR(), ld % l)
            dstd = "%s%s" % (langpackpath, ld % l)
            if shelltools.isDirectory(srcd):
                if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
                shelltools.move(srcd, dstd)

        srcf = "%s/usr/share/doc/libreoffice/README_%s" % (get.installDIR(), l)
        dstd = "%s/usr/share/doc/libreoffice" % langpackpath
        dstf = "%s/README_%s" % (dstd, l)
        if shelltools.isFile(srcf):
            if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
            shelltools.move(srcf, dstf)

        srcd = "%s/usr/lib/libreoffice/program/resource" % get.installDIR()
        dstd = "%s/usr/lib/libreoffice/program/resource" % langpackpath
        for f in os.listdir(srcd):
            if l == "id" and f.endswith("s%s.res" % l): continue
            elif l == "st" and f.endswith("a%s.res" % l): continue
            elif f.endswith("%s.res" % l):
                if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
                shelltools.move("%s/%s" % (srcd, f), dstd)

        for path in ("/usr/lib/libreoffice/share/registry", "/usr/lib/libreoffice/share/registry/res"):
            srcd = "%s%s" % (get.installDIR(), path)
            dstd = "%s%s" % (langpackpath, path)
            for f in os.listdir(srcd):
                if l == "id" and f.endswith("s%s.xcd" % l): continue
                elif l == "ss" and f == "impress.xcd": continue
                elif l == "st" and f.endswith("a%s.xcd" % l): continue
                elif l == "th" and f == "math.xcd": continue
                elif f.endswith("%s.xcd" % l):
                    if not shelltools.isDirectory(dstd): shelltools.makedirs(dstd)
                    shelltools.move("%s/%s" % (srcd, f), dstd)

    for i in ["readmes/README_*", "CREDITS*", "LICENSE*", "NOTICE*"]:
        pisitools.domove("/usr/lib/libreoffice/%s" % i, "/usr/share/doc/libreoffice")
    pisitools.removeDir("/usr/lib/libreoffice/readmes")

    print("creating: %s.tar.xz" % langpackdir)
    shelltools.cd("%s/../" % get.installDIR())
    shelltools.system("tar c %s | xz -9 > %s.tar.xz" % ((langpackdir, )*2))


