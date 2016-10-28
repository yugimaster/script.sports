# -*- coding: utf8 -*-

import os
import sys
import xbmc
import xbmcaddon


ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_ICON = ADDON.getAddonInfo('icon')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_DATA_PATH = xbmc.translatePath("special://profile/addon_data/%s" % ADDON_ID).decode("utf-8")
sys.path.append(xbmc.translatePath(os.path.join(ADDON_PATH, 'resources', 'lib')))
from WindowManager import wm
import MyFont


class Main:

    def __init__(self):
        xbmc.log("version %s started" % ADDON_VERSION)
        MyFont.addFont("font_sport24", "msyh.ttf", "24")
        MyFont.addFont("font_sport26", "msyh.ttf", "26")
        MyFont.addFont("font_sport28", "msyh.ttf", "28")
        MyFont.addFont("font_sport30", "msyh.ttf", "30")
        MyFont.addFont("font_sport32", "msyh.ttf", "32")
        MyFont.addFont("font_sport36", "msyh.ttf", "36")
        MyFont.addFont("font_sportbd24", "msyhbd.ttf", "24")
        MyFont.addFont("font_sportbd30", "msyhbd.ttf", "30")
        MyFont.addFont("font_sportbd32", "msyhbd.ttf", "32")
        MyFont.addFont("font_sportbd33", "msyhbd.ttf", "33")
        MyFont.addFont("font_sportbd36", "msyhbd.ttf", "36")
        MyFont.addFont("font_sportbd40", "msyhbd.ttf", "40")
        MyFont.addFont("font_sportbd42", "msyhbd.ttf", "42")
        MyFont.addFont("font_sportbd48", "msyhbd.ttf", "48")
        wm.open_main_window()

if (__name__ == "__main__"):
    Main()
xbmc.log('finished')
