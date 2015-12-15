#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import qt5

#WorkDir = "QScintilla-gpl-%s" % get.srcVERSION()
NoStrip = ["/usr/share/doc"]

def setup():
    shelltools.copy("./designer-Qt4Qt5/qscintillaplugin.h", "./Qt4Qt5/Qsci/")
    shelltools.cd("Qt4Qt5")
    qt5.configure()

    # Change C/XXFLAGS
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

    # Get designer plugin's Makefile
    shelltools.cd("../designer-Qt4Qt5/")
    qt5.configure()

    # Change C/XXFLAGS of designer plugin's makefile
    pisitools.dosed("Makefile", "^CFLAGS.*\\$\\(DEFINES\\)", "CFLAGS   = %s -fPIC $(DEFINES)" % get.CFLAGS())
    pisitools.dosed("Makefile", "^CXXFLAGS.*\\$\\(DEFINES\\)", "CXXFLAGS   = %s -fPIC $(DEFINES)" % get.CXXFLAGS())

def build():
    shelltools.cd("Qt4Qt5")
    #autotools.make("all staticlib CC=\"%s\" CXX=\"%s\" LINK=\"%s\"" % (get.CC(), get.CXX(), get.CXX()))
    qt5.make()

    shelltools.cd("../designer-Qt4Qt5/")
    #autotools.make("DESTDIR=\"%s/%s/designer\"" % (get.installDIR(), qt5.plugindir))
    shelltools.system("qmake-qt5 designer.pro INCLUDEPATH+=../Qt4Qt5 QMAKE_LIBDIR+=../Qt4Qt5")
    

    ## Get Makefile of qscintilla-python via sip
    shelltools.copytree("../Python", "../Python3")
    shelltools.cd("../Python")
    pythonmodules.run("configure.py -n ../Qt4Qt5/ -o ../Qt4Qt5/ -c --pyqt=PyQt5 --pyqt-sipdir=/usr/share/sip/Py2Qt5 --qsci-sipdir=/usr/share/sip/Py2Qt5 --qmake /usr/bin/qmake-qt5")
    #autotools.make()
    #qt5.make()

    shelltools.cd("../Python3")
    pythonmodules.run("configure.py -n ../Qt4Qt5/ -o ../Qt4Qt5/ -c --sip-incdir=/usr/include/python3.4m --pyqt=PyQt5  --qmake /usr/bin/qmake-qt5  --qsci-sipdir=/usr/share/sip/PyQt5 --destdir=/usr/lib/python3.4/site-packages/PyQt5", pyVer = "3")
    #pisitools.dosed("Makefile", "-lpython3.4", "-lpython3"
    #autotools.make()

def install():
    shelltools.cd("Qt4Qt5")
    qt5.install()

    shelltools.cd("../designer-Qt4Qt5/")
    qt5.install()

    #build and install qscintilla-python
    shelltools.cd("../Python3")
    autotools.install("DESTDIR=%s" % get.installDIR())
    #pythonmodules.install("--prefix=/usr") 
    shelltools.cd("../Python")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pythonmodules.install("--prefix=/usr") 

    shelltools.cd("..")
    pisitools.dohtml("doc/html-Qt4Qt5/")
    pisitools.insinto("/usr/share/doc/%s/Scintilla" % get.srcNAME(), "doc/Scintilla/*")

    #pisitools.removeDir("/usr/share/qt4")

    pisitools.dodoc("LICENSE*", "NEWS", "README")
