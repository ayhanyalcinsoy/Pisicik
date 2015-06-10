# -*- coding: utf-8 -*-
serviceType = "local"
serviceDesc = _({"en": "Lxqt network management",
                 "tr": "Lxqt ağ yönetimi"})
serviceConf = "connman"

from comar.service import *

@synchronized
def start():
    startService(command="/usr/bin/lxqt-connman-applet",
                 donotify=True)
                 #args=config.get("ATIEVENTSDOPTS", ""),

@synchronized
def stop():
    stopService(command="/usr/bin/lxqt-connman-applet",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/bin/lxqt-connman-applet")
