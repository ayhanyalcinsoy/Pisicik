#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 The Chakra Project
#
# This is a fork of Pardus's Kaptan, which is
# Copyright (C) 2006-2009 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PyKDE
from PyKDE4.kdecore import KAboutData, ki18n

# Application Data
appName     = "kaptan"
programName = ki18n("Kaptan")
modName     = "kaptan"
version     = "2013.02"
description = ki18n("Kaptan")
license     = KAboutData.License_GPL
copyright   = ki18n("(c) 2013 The Chakra Developers")
text        = ki18n(" ")
homePage    = "http://gitorious.org/chakra/kaptan"
bugEmail    = "pisilinux.org"
catalog     = appName
aboutData   = KAboutData(appName, catalog, programName, version, description, license, copyright, text, homePage, bugEmail)

# Author(s)
aboutData.addAuthor(ki18n("george"), ki18n("Current Maintainer"))
