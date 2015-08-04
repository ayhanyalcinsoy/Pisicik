#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/lxqt/themes/Ambiance', glob.glob('Ambiance/*')),
    ('/usr/share/lxqt/themes/Frost', glob.glob('Frost/*')),
    ('/usr/share/lxqt/themes/Dark', glob.glob('Dark/*')),
    ('/usr/share/lxqt/themes/Light', glob.glob('Light/*')),
    ('/usr/share/lxqt/themes/Kde-plasma', glob.glob('Kde-plasma/*')),
    ('/etc/lxqt/', glob.glob('lxqt/*')),
    ('/etc/pcmanfm-qt/lxqt/', glob.glob('pcmanfm-qt/lxqt/*')),
    ]
    #('/usr/share/lxdm/themes/lxdm-pisilinux-theme', glob.glob('lxdm/login.png')),
setup(
    name = 'pisilinux-default-settings-lxqt',
    version = '0.2',
    data_files = datas,
    )
