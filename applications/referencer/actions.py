#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
#from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/referencer/work/ and:
# WorkDir="referencer-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    autotools.configure("--disable-update-mime-database")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("referencer")

# You can use these as variables, they will replace GUI values before build.
# Package Name : referencer
# Version : 2.10
# Summary : Referencer is a GNOME application to organize documents or references, and ultimately generate a BibTeX bibliography file.

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

