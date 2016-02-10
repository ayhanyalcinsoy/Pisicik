from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Disk Management Service",
                 "tr": "Disk Yönetim Servisi"})
serviceDefault = "on"

PIDFILE="/run/udisks2.pid"
DAEMON ="/usr/libexec/udisks2/udisksd"

@synchronized
def start():
  
    startService(command=DAEMON,
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)
    
    os.system("pidof udisks2 + /usr/libexec/udisks2/udisksd > /run/udisks2.pid")
    
@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def status():
    return isServiceRunning(pidfile=PIDFILE)
