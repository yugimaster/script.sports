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
C_LIST_TIME = 301
C_LIST_SCHEDULE = 302


class MatchScheduleTimeWin(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(MatchScheduleTimeWin, self).__init__(*args, **kwargs)
        self.last_pos = 6

    def onInit(self):
        self.window_id = xbmcgui.getCurrentWindowId()
        self.window = xbmcgui.Window(self.window_id)
        self.set_match_schedule()

    def onAction(self, action):
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(MatchScheduleTimeWin, self).onClick(control_id)
        ch.serve(control_id, self)

    def set_match_schedule(self):
        now_time = time.time()
        ymd = SecondtoYMD(now_time)
        time_list = LIBRARY.fetch_match_time(now_time)
        self.set_container(C_LIST_TIME, time_list, True)
        self.getControl(C_LIST_TIME).selectItem(6)
        schedule_list = self.init_schedule_list(ymd, ymd)
        if self.window.getProperty("ScheduleTips") != "1":
            self.set_container(C_LIST_SCHEDULE, schedule_list)

    def init_schedule_list(self, startDate, endDate):
        data = LIBRARY.fetch_schedule_list(startDate, endDate)
        if not data:
            self.window.setProperty("ScheduleTips", "1")
            listitem = {}
            yield listitem
        else:
            self.window.clearProperty("ScheduleTips")
            for item in data:
                str_time = item['strMatchTime']
                iMatchState = item['iMatchState']
                if iMatchState == 0:
                    goal = "--"
                    sLiveState = u"[COLOR FF26B6F4]未开始[/COLOR]"
                elif iMatchState in [1, 2]:
                    goal = item['strLeftGoal'] + ":" + item['strRightGoal']
                    if iMatchState == 1:
                        sLiveState = u"[COLOR FFFF3939]正在直播[/COLOR]"
                    else:
                        sLiveState = u"[COLOR FF27BA9C]回看[/COLOR]"
                listitem = {"CompetitionId": item['strCompetitionId'],
                            "LeftName": item['strLeftName'],
                            "LeftBadgeLogo": item['strLeftBadge'],
                            "RightName": item['strRightName'],
                            "RightBadgeLogo": item['strRightBadge'],
                            "LiveState": sLiveState,
                            "MatchTime": str_time[-5:],
                            "MatchDesc": item['strMatchDesc'],
                            "MatchId": item['strMatchId'],
                            "MatchType": item['strMatchType'],
                            "MatchState": str(iMatchState),
                            "MatchGoal": goal
                            }
                yield listitem

    @ch.click(C_LIST_TIME)
    def schedule_list_click(self):
        lastitem = self.getControl(C_LIST_TIME).getListItem(self.last_pos)
        lastitem.setProperty("current", "0")
        self.last_pos = self.getControl(C_LIST_TIME).getSelectedPosition()
        item = self.getControl(C_LIST_TIME).getSelectedItem()
        item.setProperty("current", "1")
        ymd = item.getProperty("ymd")
        lists = self.init_schedule_list(ymd, ymd)
        self.set_container(C_LIST_SCHEDULE, lists)

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
