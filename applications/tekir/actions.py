#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def install():
    shelltools.cd(".")
    pisitools.insinto("/opt/jboss6/server/default/deploy", "./tekir/tekir.ear")
    pisitools.insinto("/opt/jboss6/server/default/deploy", "./tekir/tekir-ds.xml")
    pisitools.insinto("/opt/jboss6/server/default/deploy", "./tekir/tekir-mail-service.xml")
    pisitools.insinto("/opt/jboss6/server/default/conf", "./tekir/tekir.properties")
    pisitools.insinto("/opt/jboss6/server/default/lib", "./lib/mysql.jar")
    pisitools.dodir("/var/tekir/sablonlar")
    pisitools.dodir("/var/tekir/dosyalar")
    pisitools.insinto("/var/tekir", "./tekir/sablonlar/")