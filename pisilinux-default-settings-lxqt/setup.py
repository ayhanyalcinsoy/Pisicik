#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/lxqt/themes/a-mego', glob.glob('a-mego/*')),
    ('/usr/share/lxqt/themes/ambiance', glob.glob('ambiance/*')),
    ('/usr/share/lxqt/themes/flat', glob.glob('flat/*')),
    ('/usr/share/lxqt/themes/flat-dark-alpha', glob.glob('flat-dark-alpha/*')),
    ('/usr/share/lxqt/themes/light', glob.glob('light/*')),
    ('/usr/share/lxqt/themes/green', glob.glob('green/*')),
    ('/usr/share/lxqt/themes/plasma-next-alpha', glob.glob('plasma-next-alpha/*')),
    ('/etc/lxqt/', glob.glob('lxqt/*')),
    ('/etc/pcmanfm-qt/lxqt/', glob.glob('pcmanfm-qt/lxqt/*')),
    ]

setup(
    name = 'pisilinux-default-settings-lxqt',
    version = '0.1',
    data_files = datas,
    )
