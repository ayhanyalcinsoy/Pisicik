#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    #Installing Nautilus extension
    pisitools.insinto("usr/lib/nautilus-python/extensions/", "clients/nautilus-3.0/RabbitVCS.py")
    # Installing Thunar Extension
    pisitools.insinto("usr/lib/thunarx-2/python/", "clients/thunar/RabbitVCS.py")
    # Installing Gedit Extension
    pisitools.insinto("usr/lib/gedit/plugins", "clients/gedit/rabbitvcs-plugin.py")
    pisitools.insinto("usr/lib/gedit/plugins", "clients/gedit/rabbitvcs-gedit3.plugin")
    pisitools.insinto("usr/lib/gedit/plugins", "clients/gedit/rabbitvcs-gedit2.gedit-plugin")
    # Installing Caja extension
    pisitools.insinto("usr/lib/caja/extensions-2.0/python", "clients/caja/RabbitVCS.py")
    # Installing CLI Extension
    pisitools.insinto("usr/bin", "clients/cli/rabbitvcs")
