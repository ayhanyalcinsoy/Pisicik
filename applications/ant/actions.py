#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
import glob

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
shelltools.export("ANT_HOME", "/usr/share/ant")

WorkDir = "apache-ant-%s" % get.srcVERSION()
anthome = "/usr/share/ant"
javadir = "/usr/share/java"

def build():
    shelltools.export("ANT_OPTS", "-Duser.home=%s" % WorkDir)    
    shelltools.system("./bootstrap.sh")
def install():
    
    for d in (anthome, os.path.join(anthome, "lib"), os.path.join(anthome, "etc"), os.path.join(anthome, "bin"), javadir, os.path.join(javadir, "ant")):
        pisitools.dodir(d)
        
    shelltools.cd("build/lib")
    pisitools.insinto("/usr/share/java", "*.jar")
    pisitools.insinto("/usr/share/java", "%s/apache-ant-%s/lib/optional/hamcrest-core-1.3.jar" % (get.workDIR(), get.srcVERSION()), "hamcrest.jar")
    pisitools.insinto("/usr/share/java", "%s/apache-ant-%s/lib/optional/junit-4.11.jar" % (get.workDIR(), get.srcVERSION()), "junit.jar")
    pisitools.insinto("/usr/share/ant/lib", "*.jar")
    #pisitools.insinto("/usr/share/java", "%s/apache-ant-%s/junit-4.12-sources.jar" % (get.workDIR(), get.srcVERSION()))
    #pisitools.dosym("/usr/share/java/junit-4.12-sources.jar", "/usr/share/java/junit.jar")
    #pisitools.remove("/usr/share/java/ant-junit.jar")
    
    shelltools.cd("../../src/script")
    for f in glob.glob("*.bat"):
        shelltools.unlink(f)

    for f in glob.glob("*.cmd"):
        shelltools.unlink(f)

    pisitools.dobin("*")
    pisitools.domove("/usr/bin/antRun*", os.path.join(anthome, "bin"))
    shelltools.cd("../../")

    #Install XSLs
    pisitools.insinto(os.path.join(anthome, "etc"), "src/etc/*.xsl")
    pisitools.insinto("/etc/ant", "src/etc/*.xsl")

    pisitools.dodoc("KEYS", "NOTICE", "README", "WHATSNEW", "LICENSE")
    #pisitools.dohtml("docs/*")
