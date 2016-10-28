# -*- coding: utf-8 -*-

import xbmcgui
from BaseClasses import *
from dialogs.DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
from library import LibraryFunctions
from Utils import *

ch = OnClickHandler()
LIBRARY = LibraryFunctions()
C_LIST_FILTER = 401


class AccountWin(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(AccountWin, self).__init__(*args, **kwargs)
        self.last_pos = 6

    def onInit(self):
        self.window_id = xbmcgui.getCurrentWindowId()
        self.window = xbmcgui.Window(self.window_id)
        self.set_filter_list()

    def onAction(self, action):
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(AccountWin, self).onClick(control_id)
        ch.serve(control_id, self)

    def set_filter_list(self):
        lists = self.init_filter_list()
        self.set_container(C_LIST_FILTER, lists, True)

    def init_filter_list(self):
        listitem = {"label": u"用户",
                    "name": "account"}
        yield listitem
        listitem = {"label": u"预约",
                    "name": "order"}
        yield listitem

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
