import re
import os
import shutil

def postInstall():
    uri_enable('/tekir=loadbalancer')
    uri_enable('/tekir/*=loadbalancer')
    copyTekirDB()

def preRemove():
    uri_disable('/tekir=loadbalancer')
    uri_disable('/tekir/*=loadbalancer')

def uri_enable(uri):
    s = open('/etc/apache2/uriworkermap.properties').read()
    uris = re.findall(uri, s)

    if uri not in uris:
        open('/etc/apache2/uriworkermap.properties', 'a').write("\n" + uri)
        return True

    return False

def uri_disable(uri):
    s = open('/etc/apache2/uriworkermap.properties').read()
    uris = re.findall(uri, s)

    if uri in uris:
        s2 = re.sub(uri, "", s)
        open('/etc/apache2/uriworkermap.properties', 'w').write(s2)
        return True

    return False

def copyTekirDB():
    if not os.path.exists("/var/db/tekir/tekirDB.log"):
        shutil.copyfile("/usr/share/tekir/tekirDB.log", "/var/db/tekir/tekirDB.log")



