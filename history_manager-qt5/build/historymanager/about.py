#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PDS Stuff
import context as ctx

PACKAGE = "History Manager"
appName = "history-manager"
version = "0.2.7.1"
homePage = "https://github.com/ayhanyalcinsoy/history_manager"
bugEmail = "admins@pisilinux.org"
if ctx.Pds.session == ctx.pds.Kde4:


    # PyKDE
    from PyKDE4.kdecore import KAboutData, ki18n, ki18nc

    # Application Data
    modName     = "historymanager"
    programName = ki18n(PACKAGE)
    description = ki18n(PACKAGE)
    license     = KAboutData.License_GPL
    copyright   = ki18n("(c) 2006-2010 TUBITAK/UEKAE")
    text        = ki18n(None)
    catalog     = appName
    aboutData   = KAboutData(appName, catalog, programName, version, description, license, copyright, text, homePage, bugEmail)

    # Author(s)
    aboutData.addAuthor (ki18n("Ayhan Yalçınsoy"), ki18n("Current Maintainer"))
    aboutData.addAuthor(ki18n("İşbaran Akçayır"), ki18n("First Developer"))
    aboutData.setTranslator(ki18nc("NAME OF TRANSLATORS", "Your names"), ki18nc("EMAIL OF TRANSLATORS", "Your emails"))

    # Use this if icon name is different than appName
    aboutData.setProgramIconName("user-away-extended")
