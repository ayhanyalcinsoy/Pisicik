#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009-2010 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file

import pisi

from PyQt5 import QtGui
from PyQt5.QtCore import *

from ui_repodialog import Ui_RepoDialog

class RepoDialog(QtGui.QDialog, Ui_RepoDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        arch = pisi.ctx.config.values.general.architecture
        self.repoAddress.addItem("http://packages.pisilinux.org/repositories/%s/stable/x86_64/pisi-index.xml.xz" % arch)

