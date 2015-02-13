#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/lxqt/themes/ambiance', glob.glob('ambiance/*')),
    ('/usr/share/lxqt/themes/frost', glob.glob('frost/*')),
    ('/usr/share/lxqt/themes/dark', glob.glob('dark/*')),
    ('/usr/share/lxqt/themes/light', glob.glob('light/*')),
    ('/usr/share/lxqt/themes/kde-plasma', glob.glob('kde-plasma/*')),
    ('/usr/share/lxdm/themes/lxdm-pisilinux-theme', glob.glob('lxdm/login.png')),
    ('/etc/lxqt/', glob.glob('lxqt/*')),
    ('/etc/pcmanfm-qt/lxqt/', glob.glob('pcmanfm-qt/lxqt/*')),
    ]

setup(
    name = 'pisilinux-default-settings-lxqt',
    version = '0.1',
    data_files = datas,
    )
