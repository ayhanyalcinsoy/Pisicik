# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    #pisitools.dodir("/opt/kingsoft/wps-office")
    #pisitools.dodir("/usr/share/fonts/wps-office")
    pisitools.insinto("/opt/kingsoft/wps-office/","office6")
    pisitools.insinto("/usr/bin/", "wps")
    pisitools.insinto("/usr/bin/", "wpp")
    pisitools.insinto("/usr/bin/", "et")
    pisitools.insinto("/usr/bin/", "wps_error_check.sh")
    pisitools.insinto("/usr/share/applications/", "resource/applications/*desktop")
    pisitools.insinto("/usr/share/icons/", "resource/icons/*")
    pisitools.insinto("/usr/share/mime/", "resource/mime/*")
    pisitools.insinto("/usr/share/fonts/wps-office/", "fonts/*")
    pisitools.insinto("/usr/share/licenses/wps-office/","office6/mui/default/EULA.txt")