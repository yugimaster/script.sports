# -*- coding: utf-8 -*-

import xbmcgui
import time
from BaseClasses import *
from dialogs.DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
from library import LibraryFunctions
from Utils import *

ch = OnClickHandler()
LIBRARY = LibraryFunctions()
C_LIST_TIME = 11
C_LIST_SCHEDULE = 12


class ScheduleDetailWin(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(ScheduleDetailWin, self).__init__(*args, **kwargs)
        self.last_pos = 6

    def onInit(self):
        self.window_id = xbmcgui.getCurrentWindowId()
        self.window = xbmcgui.Window(self.window_id)
        self.set_time_tab()

    def onAction(self, action):
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(ScheduleDetailWin, self).onClick(control_id)
        ch.serve(control_id, self)

    def set_time_tab(self):
        now_time = time.time()
        ymd = SecondtoYMD(now_time)
        print "aaaa", ymd
        time_list = LIBRARY.fetch_time_tab(now_time)
        self.set_container(C_LIST_TIME, time_list, True)
        self.getControl(C_LIST_TIME).selectItem(6)
        self.set_current_date()
        schedule_list = self.init_schedule_list(ymd, ymd)
        self.set_container(C_LIST_SCHEDULE, schedule_list)

    def set_current_date(self):
        item = self.getControl(C_LIST_TIME).getListItem(self.last_pos)
        date = item.getProperty("label")
        self.window.setProperty("CurrentDate", date)

    def init_schedule_list(self, startDate, endDate):
        data = LIBRARY.fetch_schedule_list(startDate, endDate)
        if not data:
            listitem = {
                "CompetitionId": "",
                "LeftName": "",
                "LeftBadgeLogo": "",
                "LeftGoal": "",
                "RightName": "",
                "RightBadgeLogo": "",
                "RightGoal": "",
                "LiveState": "",
                "MatchDesc": u"今日无任何赛事",
                "MatchId": "",
                "MatchType": ""
            }
            yield listitem
        else:
            for item in data:
                listitem = {"CompetitionId": item['strCompetitionId'],
                            "LeftName": item['strLeftName'],
                            "LeftBadgeLogo": item['strLeftBadge'],
                            "LeftGoal": item['strLeftGoal'],
                            "RightName": item['strRightName'],
                            "RightBadgeLogo": item['strRightBadge'],
                            "RightGoal": item['strRightGoal'],
                            "LiveState": item['strLiveState'],
                            "MatchDesc": item['strMatchDesc'],
                            "MatchId": item['strMatchId'],
                            "MatchType": item['strMatchType']
                            }
                yield listitem

    @ch.click(C_LIST_TIME)
    def schedule_list_click(self):
        lastitem = self.getControl(C_LIST_TIME).getListItem(self.last_pos)
        lastitem.setProperty("current", "0")
        self.last_pos = self.getControl(C_LIST_TIME).getSelectedPosition()
        item = self.getControl(C_LIST_TIME).getSelectedItem()
        self.window.setProperty("CurrentDate", item.getProperty("label"))
        item.setProperty("current", "1")
        ymd = item.getProperty("ymd")
        lists = self.init_schedule_list(ymd, ymd)
        self.set_container(C_LIST_SCHEDULE, lists)

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
