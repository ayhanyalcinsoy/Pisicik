#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from distutils.core import setup

datas = [
    ('/usr/share/lxde/wallpapers/', glob.glob('lxde/data/pisilinux3d.jpg')),
    ('/usr/share/applications/', glob.glob('lxde/data/lxde-lock-screen.desktop')),
    ('/usr/share/lxde/wallpapers/', glob.glob('lxde/data/lxde-pisilinux.png')),
    ('/usr/share/lxde/wallpapers/', glob.glob('lxde/data/pisilinux-blue.png')),
    ('/usr/share/lxde/images/', glob.glob('lxde/data/lxde_pisilinux2012_menu.png')),
    ('/usr/share/lxde/images/', glob.glob('lxde/data/pisilinuxLogo.png')),
    ('/usr/share/lxpanel/images/', glob.glob('lxde/data/background-pisilinux.png')),
    ('/usr/share/lxde/images/', glob.glob('lxde/data/logout-banner.png')),
    ('/etc/xdg/pcmanfm/LXDE/', glob.glob('pcmanfm/lxde/*')),
    ('/etc/xdg/lxsession/LXDE/', glob.glob('lxsession/*')),
    ('/etc/xdg/lxsession/LXDE/', glob.glob('lxsession/*')),
    ('/etc/xdg/openbox/LXDE/', glob.glob('openbox/*')),
    ('/etc/xdg/lxpanel/LXDE/', glob.glob('lxpanel/config')),
    ('/etc/xdg/lxpanel/LXDE/panels/', glob.glob('lxpanel/panel')),
    ('/usr/share/applications/', glob.glob('lxpanel/data/lxde-logout.desktop')),
    ('/usr/share/applications/', glob.glob('lxpanel/data/lxde-screenlock.desktop')),
    ('/usr/share/applications/', glob.glob('lxpanel/data/lxde-x-terminal-emulator.desktop')),
    ('/usr/share/lxde/images/', glob.glob('lxpanel/data/pisi_striped_blue.png')),
    ('/usr/share/lxdm/themes/lxdm-pisilinux-theme', glob.glob('lxdm/login.png')),
    ]

setup(
    name = 'pisilinux-default-settings-lxde',
    version = '0.1',
    data_files = datas,
    )
