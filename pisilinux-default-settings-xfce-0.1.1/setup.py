#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/backgrounds/xfce', glob.glob('wallpaper/*')),
    ('/etc/xdg/xfce4/xfconf/xfce-perchannel-xml', glob.glob('xfce-perchannel-xml/*')),
    ('/etc/xdg/xfce4/terminal', glob.glob('terminal/*')),
    ]

setup(
    name = 'pisilinux-default-settings-xfce',
    version = '0.1',
    data_files = datas,
    )
