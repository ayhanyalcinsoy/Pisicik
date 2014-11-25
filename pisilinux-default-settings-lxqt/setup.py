#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/lxqt/themes/', glob.glob('usr/share/lxqt/themes/*')),
    ('/etc/lxqt/', glob.glob('etc/lxqt/*')),
    ('/etc/pcmanfm-qt/lxqt/', glob.glob('etc/pcmanfm-qt/lxqt/*')),
    ]

setup(
    name = 'pisilinux-default-settings-lxqt',
    version = '0.1',
    data_files = datas,
    )
