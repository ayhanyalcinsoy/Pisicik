# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
KDIR = kerneltools.getKernelVersion()
NoStrip = ["/lib/modules"]

BuildDir = "common/lib/modules/fglrx/build_mod"

if get.buildTYPE() == 'emul32':
    Target = "x86"
    Libdir = "/usr/lib32"
else:
    Target = get.ARCH().replace("i686", "x86")
    Libdir = "/usr/lib"

XDir = "xpic" + ("_64a" if Target == "x86_64" else "")


def setup():
    shelltools.export("SETUP_NOCHECK", "1")
    shelltools.system("sh %s/fglrx-15.302/amd-driver-installer-*-x86.x86_64.run --extract ." % get.workDIR())


def install():
    ##catalyst-utils section
  ## Install userspace tools and libraries
    # Create directories
    pisitools.dodir("/etc/ati")
    pisitools.dodir("/etc/rc.d")
    pisitools.dodir("/etc/profile.d")
    pisitools.dodir("/etc/acpi/events")
    pisitools.dodir("/etc/security/console.apps")
    pisitools.dodir("/etc/OpenCL/vendors")

    pisitools.dodir("/usr/lib/xorg/modules/dri")
    pisitools.dodir("/usr/lib/xorg/modules/drivers")
    pisitools.dodir("/usr/lib/xorg/modules/extensions")
    pisitools.dodir("/usr/lib/xorg/modules/extensions/fglrx")
    pisitools.dodir("/usr/lib/xorg/modules/linux")
    pisitools.dodir("/usr/lib/dri")
    pisitools.dodir("/usr/lib/fglrx")
    pisitools.dodir("/usr/lib/systemd/system")
    pisitools.dodir("/usr/lib32")
#       pisitools.dodir("/usr/lib/hsa		#removed in 14.1

    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/include/GL")

    pisitools.dodir("/usr/share/applications")
    pisitools.dodir("/usr/share/ati/amdcccle")
    pisitools.dodir("/usr/share/licenses/catalyst")
    pisitools.dodir("/usr/share/man/man8")
    pisitools.dodir("/usr/share/pixmaps")

    # X.org driver
    if get.buildTYPE() == "emul32":
        shelltools.cd("xpic/usr/X11R6/lib/modules")
        pisitools.insinto("/usr/lib32/xorg/modules", "*.so")
        pisitools.insinto("/usr/lib32/xorg/modules/drivers", "drivers/*.so")
        pisitools.insinto("/usr/lib32/xorg/modules/linux", "linux/*.so")
        pisitools.insinto("/usr/lib32/xorg/modules/extensions/fglrx", "extensions/fglrx/fglrx-libglx.so")
        pisitools.dosym("/usr/lib32/xorg/modules/extensions/fglrx/fglrx-libglx.so", "/usr/lib32/xorg/modules/extensions/libglx.so")
        return

    if not get.buildTYPE() == 'emul32':
        shelltools.cd("xpic_64a/usr/X11R6/lib64/modules")
        pisitools.insinto("/usr/lib/xorg/modules", "*.so")
        pisitools.insinto("/usr/lib/xorg/modules/drivers", "drivers/*.so")
        pisitools.insinto("/usr/lib/xorg/modules/linux", "linux/*.so")
        pisitools.insinto("/usr/lib/xorg/modules/extensions/fglrx", "extensions/fglrx/fglrx-libglx.so")
        #pisitools.dosym("/usr/lib/xorg/modules/extensions/fglrx/fglrx-libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")

    # Controlcenter / libraries
    if get.buildTYPE() == "emul32":
        #shelltools.cd("%s" % get.workDIR())
        shelltools.cd("arch/x86/usr")
        pisitools.insinto("/usr/bin", "X11R6/bin/*")
        pisitools.insinto("/usr/bin", "sbin/*")
        pisitools.insinto("/usr/lib32/fglrx", "X11R6/lib/fglrx/fglrx-libGL.so.1.2")
        pisitools.insinto("/usr/lib32", "X11R6/lib/libAMDXvBA.so.1.0")
        pisitools.dosym("/usr/lib32/libAMDXvBA.so.1.0", "/usr/lib/libAMDXvBA.so.1")
        pisitools.dosym("/usr/lib32/libAMDXvBA.so.1.0", "/usr/lib/libAMDXvBA.so")
        pisitools.insinto("/usr/lib32", "X11R6/lib/libatiadlxx.so")
        pisitools.insinto("/usr/lib32", "X11R6/lib/libfglrx_dm.so.1.0")
        pisitools.insinto("/usr/lib32", "X11R6/lib/libXvBAW.so.1.0")
        pisitools.dosym("/usr/lib32/libXvBAW.so.1.0", "/usr/lib/libXvBAW.so.1")
        pisitools.dosym("/usr/lib32/libXvBAW.so.1.0", "/usr/lib/libXvBAW.so")
        pisitools.dosym("/usr/lib32/libXvBAW.so.1.0", "/usr/lib/dri/fglrx_drv_video.so") #omega 14.12
        pisitools.insinto("/usr/lib32", "X11R6/lib/*.a")
        pisitools.insinto("/usr/lib32", "X11R6/lib/*.cap")
        pisitools.insinto("/usr/lib32/xorg/modules/dri", "X11R6/lib/modules/dri/*.so")
        pisitools.insinto("/usr/lib32", "lib/*.so*")
        pisitools.dodir("/usr/share/ati/lib32")
        pisitools.insinto("/usr/share/ati/lib32", "share/ati/lib/*.so*")
        
    if not get.buildTYPE() == 'emul32':
        shelltools.cd("%s/arch/x86_64/usr" % get.workDIR())
        pisitools.insinto("/usr/bin", "X11R6/bin/*")
        pisitools.insinto("/usr/bin", "sbin/*")
        pisitools.insinto("/usr/lib/fglrx", "X11R6/lib64/fglrx/fglrx-libGL.so.1.2")
        pisitools.insinto("/usr/lib", "X11R6/lib64/libAMDXvBA.so.1.0")
        pisitools.dosym("/usr/lib/libAMDXvBA.so.1.0", "/usr/lib/libAMDXvBA.so.1")
        pisitools.dosym("/usr/lib/libAMDXvBA.so.1.0", "/usr/lib/libAMDXvBA.so")
        pisitools.insinto("/usr/lib", "X11R6/lib64/libatiadlxx.so")
        pisitools.insinto("/usr/lib", "X11R6/lib64/libfglrx_dm.so.1.0")
        pisitools.insinto("/usr/lib", "X11R6/lib64/libXvBAW.so.1.0")
        pisitools.dosym("/usr/lib/libXvBAW.so.1.0", "/usr/lib/libXvBAW.so.1")
        pisitools.dosym("/usr/lib/libXvBAW.so.1.0", "/usr/lib/libXvBAW.so")
        pisitools.dosym("/usr/lib/libXvBAW.so.1.0", "/usr/lib/dri/fglrx_drv_video.so") #omega 14.12
        pisitools.insinto("/usr/lib", "X11R6/lib64/*.a")
        pisitools.insinto("/usr/lib", "X11R6/lib64/*.cap")
        pisitools.insinto("/usr/lib/xorg/modules/dri", "X11R6/lib64/modules/dri/*.so")
        pisitools.insinto("/usr/lib", "lib64/*.so*")
#       install -m755 ${_lib}/hsa/* ${pkgdir}/usr/lib/hsa		#removed in 14.1

    ## QT libs (only 2 files) - un-comment 2 lines below if you don't want to install qt package
        pisitools.dodir("/usr/share/ati/lib")
        pisitools.insinto("/usr/share/ati/lib", "share/ati/lib64/*.so*")
        
    pisitools.dosym("/usr/lib/xorg/modules/dri/fglrx_dri.so", "/usr/lib/dri/fglrx_dri.so")
    pisitools.dosym("/usr/lib/xorg/modules/dri/libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so.1")
    pisitools.dosym("/usr/lib/xorg/modules/dri/libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so")
    pisitools.dosym("/usr/lib/xorg/modules/dri/libatiuki.so.1.0", "/usr/lib/libatiuki.so.1")
    pisitools.dosym("/usr/lib/xorg/modules/dri/libatiuki.so.1.0", "/usr/lib/libatiuki.so")
    pisitools.dosym("/usr/lib/xorg/modules/dri/libOpenCL.so.1", "/usr/lib/libOpenCL.so")
    
    pisitools.dosym("/usr/lib/fglrx/fglrx-libGL.so.1.2", "/usr/lib/fglrx/libGL.so.1.2.0")
    pisitools.dosym("/usr/lib/fglrx/fglrx-libGL.so.1.2", "/usr/lib/fglrx/libGL.so.1")
    pisitools.dosym("/usr/lib/fglrx/fglrx-libGL.so.1.2", "/usr/lib/fglrx/libGL.so")
    pisitools.dosym("/usr/lib/fglrx/fglrx-libGL.so.1.2", "/usr/lib/libGL.so.1.2.0")
    #pisitools.dosym("/usr/lib/fglrx/fglrx-libGL.so.1.2", "/usr/lib/libGL.so.1")
    #pisitools.dosym("/usr/lib/fglrx/fglrx-libGL.so.1.2", "/usr/lib/libGL.so")

      # We have to provide symlinks to mesa, as catalyst doesn't ship them
    #pisitools.dosym("/usr/lib/mesa/libEGL.so.1.0.0", "/usr/lib/libEGL.so.1.0.0")
    #pisitools.dosym("/usr/lib/mesalibEGL.so.1.0.0", "/usr/lib/libEGL.so.1")
    #pisitools.dosym("/usr/lib/mesalibEGL.so.1.0.0", "/usr/lib/libEGL.so")

    #pisitools.dosym("/usr/lib/mesa/libGLESv1_CM.so.1.1.0","/usr/lib/libGLESv1_CM.so.1.1.0")
    #pisitools.dosym("/usr/lib/mesa/libGLESv1_CM.so.1.1.0", "/usr/lib/libGLESv1_CM.so.1")
    #pisitools.dosym("/usr/lib/mesa/libGLESv1_CM.so.1.1.0", "/usr/lib/libGLESv1_CM.so")

    #pisitools.dosym("/usr/lib/mesa/libGLESv2.so.2.0.0", "/usr/lib/libGLESv2.so.2.0.0")
    #pisitools.dosym("/usr/lib/mesa/libGLESv2.so.2.0.0", "/usr/lib/libGLESv2.so.2")
    #pisitools.dosym("/usr/lib/mesa/libGLESv2.so.2.0.0", "/usr/lib/libGLESv2.so")


    shelltools.cd("%s/common" % get.workDIR())
    pisitools.insinto("/etc/ati", "etc/ati/*")
    shelltools.chmod("etc/ati/authatieventsd.sh", 0755)

    pisitools.insinto("/etc/security/console.apps", "etc/security/console.apps/amdcccle-su")

    pisitools.insinto("/usr/bin", "usr/X11R6/bin/*")
    pisitools.insinto("/usr/include/GL", "usr/include/GL/*.h")
    pisitools.insinto("/usr/bin", "usr/sbin/*.sh")
    pisitools.insinto("/usr/share/ati/amdcccle", "usr/share/ati/amdcccle/*")
    pisitools.insinto("/usr/share/pixmaps", "usr/share/icons/*.xpm")
    pisitools.insinto("/usr/share/man/man8", "usr/share/man/man8/*.8")
    pisitools.insinto("/usr/share/applications", "usr/share/applications/*.desktop")

    # ACPI example files
#       install -m755 usr/share/doc/fglrx/examples/etc/acpi/*.sh ${pkgdir}/etc/acpi
#       sed -i -e "s/usr\/X11R6/usr/g" ${pkgdir}/etc/acpi/ati-powermode.sh
#       install -m644 usr/share/doc/fglrx/examples/etc/acpi/events/* ${pkgdir}/etc/acpi/events
    # lets check our own files - V
    shelltools.cd("..")
    pisitools.insinto("/etc/acpi", "ati-powermode.sh")
    pisitools.insinto("/etc/acpi/events", "a-ac-aticonfig")
    pisitools.insinto("/etc/acpi/events", "a-lid-aticonfig")

    # thanks to cerebral, we dont need that damned symlink
    pisitools.insinto("/etc/profile.d", "catalyst.sh")

    # License
#       install -m644 ${srcdir}/archive_files/LICENSE.TXT ${pkgdir}/usr/share/licenses/${pkgname}
    pisitools.insinto("/usr/share/licenses/catalyst", "LICENSE.TXT")
    pisitools.insinto("/usr/share/licenses/catalyst", "common/usr/share/doc/amdcccle/ccc_copyrights.txt")

    # since 11.11 : opencl files
    if get.buildTYPE() == "emul32":
        shelltools.cd("/arch/x86")
        pisitools.insinto("/etc/OpenCL/vendors", "/etc/OpenCL/vendors/amdocl32.icd")

    
    if not get.buildTYPE() == 'emul32':
        shelltools.cd("./arch/x86_64")
        pisitools.insinto("/etc/OpenCL/vendors", "etc/OpenCL/vendors/amdocl64.icd")
        pisitools.insinto("/usr/bin", "usr/bin/clinfo")
        pisitools.dodir("/etc/modules-load.d")
        pisitools.insinto("/etc/modules-load.d", "%s/catalyst.conf" % get.workDIR())

    #workaround for the high io bug , thanks to lano1106 for finding this ugly bug! https://bbs.archlinux.org/viewtopic.php?pid=1279977#p1279977
        pisitools.insinto("/usr/bin", "%s/temp_links_catalyst" % get.workDIR())
        pisitools.insinto("/usr/lib/systemd/system", "%s/temp-links-catalyst.service" % get.workDIR())

     # powerXpress
        pisitools.insinto("/usr/lib/fglrx", "%s/switchlibGL" % get.workDIR())
        pisitools.insinto("/usr/lib/fglrx", "%s/switchlibglx" % get.workDIR())
      # switching script: switch xorg.conf + aticonfig --px-Xgpu + switchlibGL + add/remove fglrx into MODULES
        pisitools.insinto("/usr/bin", "%s/pxp_switch_catalyst" % get.workDIR())
        
        

##catalyst-hook section
    shelltools.cd("%s" % get.workDIR())
    #shelltools.system("patch -p1 < desktop-files.patch")
    shelltools.system("patch -p1 < fglrx_gpl_symbol.patch")
    #shelltools.system("patch -p1 < kolasa_4.0-cr4-strn.patch")
    shelltools.system("patch -p1 < lano1106_fglrx_intel_iommu.patch")
    shelltools.system("patch -p1 < lano1106_kcl_agp_13_4.patch")
    shelltools.system("patch -p1 < makefile_compat.patch")
    shelltools.system("patch -p1 < 4.3-kolasa-seq_printf.patch")
    shelltools.system("patch -p1 < 4.3-gentoo-mtrr.patch")
    shelltools.system("patch -p1 < 4.4-manjaro-xstate.patch")
    shelltools.system("patch -p1 < crimson_i686_xg.patch")
    shelltools.system("patch -p1 < grsec_arch.patch")
     

    # Prepare modules source files
    pisitools.dodir("/usr/share/ati/build_mod")
    pisitools.insinto("/usr/share/ati/build_mod", "common/lib/modules/fglrx/build_mod/*.c")
    pisitools.insinto("/usr/share/ati/build_mod", "common/lib/modules/fglrx/build_mod/*.h")
    pisitools.insinto("/usr/share/ati/build_mod", "common/lib/modules/fglrx/build_mod/2.6.x/Makefile")
    pisitools.insinto("/usr/share/ati/build_mod", "arch/x86_64/lib/modules/fglrx/build_mod/libfglrx_ip.a")
    pisitools.insinto("/usr/bin", "catalyst_build_module")

    # modified ati's make.sh script
    pisitools.insinto("/usr/share/ati/build_mod", "ati_make.sh")

    # hook fglrx
    pisitools.dodir("/usr/lib/initcpio/install")
    pisitools.insinto("/usr/lib/initcpio/install/fglrx", "hook-fglrx")

    # systemd service to perform fglrx module build at shutdown FIXME systemd yerine baska
    pisitools.dodir("/usr/lib/systemd/system")
    pisitools.insinto("/usr/lib/systemd/system", "catalyst-hook.service")


       # lib32-catalyst-utils section

    pisitools.insinto("/etc/profile.d","lib32-catalyst.sh")
    shelltools.cd("arch/x86/usr")
    #install -dm755 ${pkgdir}/usr/lib32/hsa		#removed in 14.1
    pisitools.insinto("/usr/lib32", "lib/*.so*")
#	install -m755 lib/hsa/* ${pkgdir}/usr/lib32/hsa		#removed in 14.1
    pisitools.insinto("/usr/lib32/fglrx", "X11R6/lib/fglrx/fglrx-libGL.so.1.2")
    pisitools.insinto("/usr/lib32", "X11R6/lib/libAMDXvBA.so.1.0")
    pisitools.insinto("/usr/lib32", "X11R6/lib/libatiadlxx.so")
    pisitools.insinto("/usr/lib32", "X11R6/lib/libfglrx_dm.so.1.0")
    pisitools.insinto("/usr/lib32", "X11R6/lib/libXvBAW.so.1.0")
    pisitools.insinto("/usr/lib32/xorg/modules/dri", "X11R6/lib/modules/dri/*.so")
    pisitools.dosym("/usr/lib32/xorg/modules/dri/fglrx_dri.so","/usr/lib32/dri/fglrx_dri.so")

	#cd $pkgdir/usr/lib32
    pisitools.dosym("/usr/lib32/libfglrx_dm.so.1.0", "/usr/lib32/libfglrx_dm.so.1")
    pisitools.dosym("/usr/lib32/libfglrx_dm.so.1.0", "/usr/lib32/libfglrx_dm.so")
    pisitools.dosym("/usr/lib32/libAMDXvBA.so.1.0", "/usr/lib32/libAMDXvBA.so.1")
    pisitools.dosym("/usr/lib32/libAMDXvBA.so.1.0", "/usr/lib32/libAMDXvBA.so")
    pisitools.dosym("/usr/lib32/libXvBAW.so.1.0", "/usr/lib32/libXvBAW.so.1")
    pisitools.dosym("/usr/lib32/libXvBAW.so.1.0", "/usr/lib32/libXvBAW.so")
    pisitools.dosym("/usr/lib32/libatiuki.so.1.0", "/usr/lib32/libatiuki.so.1")
    pisitools.dosym("/usr/lib32/libatiuki.so.1.0", "/usr/lib32/libatiuki.so")
    pisitools.dosym("/usr/lib32/libOpenCL.so.1", "/usr/lib32/libOpenCL.so")

    pisitools.dosym("/usr/lib32/fglrx/fglrx-libGL.so.1.2", "/usr/lib32/fglrx/libGL.so.1.2.0")
    pisitools.dosym("/usr/lib32/fglrx/fglrx-libGL.so.1.2", "/usr/lib32/fglrx/libGL.so.1")
    pisitools.dosym("/usr/lib32/fglrx/fglrx-libGL.so.1.2", "/usr/lib32/fglrx/libGL.so")
    pisitools.dosym("/usr/lib32/fglrx/fglrx-libGL.so.1.2", "/usr/lib32/libGL.so.1.2.0")
    #pisitools.dosym("/usr/lib32/fglrx/fglrx-libGL.so.1.2", "/usr/lib32/libGL.so.1")
    #pisitools.dosym("/usr/lib32/fglrx/fglrx-libGL.so.1.2", "/usr/lib32/libGL.so")


      # We have to provide symlinks to lib32-mesa, as catalyst doesn't ship them
    #pisitools.dosym("/usr/lib32/mesa/libEGL.so.1.0.0","/usr/lib32/libEGL.so.1.0.0")
    #pisitools.dosym("/usr/lib32/mesa/libEGL.so.1.0.0","/usr/lib32/libEGL.so.1")
    #pisitools.dosym("/usr/lib32/mesa/libEGL.so.1.0.0","/usr/lib32/libEGL.so")

    #pisitools.dosym("/usr/lib32/mesa/libGLESv1_CM.so.1.1.0", "/usr/lib32/libGLESv1_CM.so.1.1.0")
    #pisitools.dosym("/usr/lib32/mesa/libGLESv1_CM.so.1.1.0", "/usr/lib32/libGLESv1_CM.so.1")
    #pisitools.dosym("/usr/lib32/mesa/libGLESv1_CM.so.1.1.0", "/usr/lib32/libGLESv1_CM.so")

    #pisitools.dosym("/usr/lib32/mesa/libGLESv2.so.2.0.0", "/usr/lib32/libGLESv2.so.2.0.0")
    #pisitools.dosym("/usr/lib32/mesa/libGLESv2.so.2.0.0", "/usr/lib32/libGLESv2.so.2")
    #pisitools.dosym("/usr/lib32/mesa/libGLESv2.so.2.0.0", "/usr/lib32/libGLESv2.so")


    # OpenCL
    pisitools.dodir("/etc/OpenCL/vendors")
    pisitools.insinto("/etc/OpenCL/vendors", "%s/arch/x86/etc/OpenCL/vendors/amdocl32.icd" % get.workDIR())

    #LICENSE information
    pisitools.dodoc("%s/LICENSE.TXT" % get.workDIR())

    # Fix file permissions
    exec_file_suffixes = (".sh", ".so", ".so.1.2.0")
    exec_dir_suffixes = ("/bin", "/sbin", "/lib")

    import os
    for root, dirs, files in os.walk(get.installDIR()):
        for name in files:
            filePath = os.path.join(root, name)
            if os.path.islink(filePath):
                continue
            if root.endswith(exec_dir_suffixes) \
                or name.endswith(exec_file_suffixes):
                shelltools.chmod(filePath, 0755)
            else:
                shelltools.chmod(filePath, 0644)
