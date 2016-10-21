# -*- coding: utf8 -*-

import xbmc
from DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
from BaseClasses import DialogXML

ch = OnClickHandler()
C_LIST_SEASON = 21
C_LIST_FORMAT = 22
C_LIST_ROUND = 23


class MatchFilter(DialogXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(MatchFilter, self).__init__(*args, **kwargs)

    def onInit(self):
        super(MatchFilter, self).onInit()
        xbmc.log('dialog match filter init')
        self.set_season_list()
        self.set_format_list()
        self.set_round_list()

    def set_season_list(self):
        season_list = self.init_season_list()
        self.set_container(C_LIST_SEASON, season_list, True)

    def set_format_list(self):
        format_list = self.init_format_list()
        self.set_container(C_LIST_FORMAT, format_list)

    def set_round_list(self):
        round_list = self.init_round_list()
        self.set_container(C_LIST_ROUND, round_list)

    def init_season_list(self):
        listitem = {
            "label": u"1617赛季",
            "icon": "dialogs/match_filter/item_nf.png",
            "index": "1"}
        yield listitem
        listitem = {
            "label": u"1516赛季",
            "icon": "dialogs/match_filter/item_nf_5.png",
            "index": "2"}
        yield listitem
        listitem = {
            "label": u"1415赛季",
            "icon": "dialogs/match_filter/item_nf_5.png",
            "index": "3"}
        yield listitem
        listitem = {
            "label": u"1314赛季",
            "icon": "dialogs/match_filter/item_nf_3.png",
            "index": "4"}
        yield listitem

    def init_format_list(self):
        listitem = {
            "label": u"联赛",
            "icon": "dialogs/match_filter/item_nf.png",
            "index": "1"}
        yield listitem

    def init_round_list(self):
        listitem = {
            "label": "1",
            "icon": "dialogs/match_filter/item_nf.png",
            "index": "1"}
        yield listitem
        listitem = {
            "label": "2",
            "icon": "dialogs/match_filter/item_nf_5.png",
            "index": "2"}
        yield listitem

    def onAction(self, action):
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(MatchFilter, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
