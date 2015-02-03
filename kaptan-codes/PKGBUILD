#
# Desktop Packages for Chakra, part of chakra-project.org
# 
# Maintainer: george <george[at]chakra-project.org>

pkgname=kaptan
pkgver=0.4.90
pkgrel=1
pkgdesc="Chakra's desktop greeter, a fork of Pardus's Kaptan."
arch=('i686' 'x86_64')
url='http://gitorious.org/chakra/kaptan/'
screenshot='http://i.imgur.com/71aU5.png'
license=('GPLv2')
conflicts=('kaptan-git')
depends=('python2'  'kde-baseapps-konsole'  'kde-runtime'
         'kdebindings-python2' 'python2-pyqt4'  'python2-xlib'
         'python2-imaging' 'xdg-user-dirs' 'ksuperkey')
makedepends=('python2-setuptools' 'git')
optdepends=('octopi-notifier: update notifications'
            'clamav: for the security page')
source=("http://chakra-linux.org/sources/${pkgname}/${pkgname}-${pkgver}.tar.xz")
md5sums=('ad47fb92a8f863338b97aed0cee1f38d')

# create tarball: source PKGBUILD && mksource

mksource() {
    git clone -b "${pkgver}" git://gitorious.org/chakra/${pkgname}.git ${pkgname}
    pushd ${pkgname}
    popd
    rm ${pkgname}/PKGBUILD
    tar -cvJf ${pkgname}-${pkgver}.tar.xz ${pkgname}
    md5sum ${pkgname}-${pkgver}.tar.xz
}

package() {
    cd "${srcdir}/${pkgname}"
    python2 setup.py install --root="${pkgdir}"
    install -Dm755 kaptan-rootactions "${pkgdir}/usr/bin/kaptan-rootactions"
    install -Dm755 kaptan.desktop "${pkgdir}/usr/share/applications/kaptan.desktop"
    install -Dm644 data/kaptan.svgz \
        "${pkgdir}/usr/share/icons/hicolor/scalable/apps/kaptan.svgz"
    install -dm755 \
        "${pkgdir}/usr/share/kde4/apps/kaptan/kaptan/kde-themes/"
    install -Dm644 data/kde-themes/* \
        "${pkgdir}/usr/share/kde4/apps/kaptan/kaptan/kde-themes/"
    install -Dm755 kaptan-autostart.desktop \
        "${pkgdir}/usr/share/kde4/apps/kaptan/kaptan/kaptan-autostart.desktop"
    install -Dm755 data/ksuperkey.desktop \
        "${pkgdir}/usr/share/kde4/apps/kaptan/kaptan/ksuperkey.desktop"
}
