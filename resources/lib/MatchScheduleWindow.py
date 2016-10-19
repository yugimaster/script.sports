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
C_LIST_CATEGORY = 11
C_LIST_SCHEDULE = 12
C_LIST_INFOMATION = 13


class MatchScheduleWin(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(MatchScheduleWin, self).__init__(*args, **kwargs)
        self.TITLE = kwargs['name']
        self.CHANNEL = kwargs['channel']
        self.CID = kwargs['competitionId']

    def onInit(self):
        self.window_id = xbmcgui.getCurrentWindowId()
        self.window = xbmcgui.Window(self.window_id)
        self.set_match_detail()

    def onAction(self, action):
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(MatchScheduleWin, self).onClick(control_id)
        ch.serve(control_id, self)

    def set_match_detail(self):
        now_time = time.time()
        start_ymd = SecondtoYMD(now_time - 86400 * 6)
        end_ymd = SecondtoYMD(now_time + 86400 * 6)
        self.window.setProperty("MatchIcon", "detail/match_icon/icon_{0}.png".format(self.CHANNEL))
        self.window.setProperty("MatchName", self.TITLE)
        category_list = self.init_category_list(self.CID, self.CHANNEL)
        self.set_container(C_LIST_CATEGORY, category_list, True)
        schedule_list = self.init_schedule_list(start_ymd, end_ymd, self.CID)
        self.set_container(C_LIST_SCHEDULE, schedule_list)
        info_list = self.init_infomation_list()
        self.set_container(C_LIST_INFOMATION, info_list)

    def set_current_date(self):
        item = self.getControl(C_LIST_CATEGORY).getListItem(self.last_pos)
        date = item.getProperty("label")
        self.window.setProperty("CurrentDate", date)

    def init_category_list(self, competitionId, channel):
        if channel == "laliga":
            listitems = [
                {"label": u"赛程", "name": "schedule", "icon": "detail/2_fo.png"},
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"集锦", "name": "collection", "icon": "detail/2_fo.png"},
                {"label": u"西甲世界", "name": "none", "icon": "detail/4_fo.png"},
                {"label": u"西甲深呼吸", "name": "none", "icon": "detail/5_fo.png"},
                {"label": u"西甲塔帕斯", "name": "none", "icon": "detail/5_fo.png"},
                {"label": u"情迷斗牛士", "name": "none", "icon": "detail/5_fo.png"}]
        elif channel == "pl":
            listitems = [
                {"label": u"集锦", "name": "collection", "icon": "detail/2_fo.png"},
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"英超秀", "name": "none", "icon": "detail/4_fo.png"},
                {"label": u"十分英超", "name": "none", "icon": "detail/4_fo.png"}]
        elif channel == "column":
            listitems = [
                {"label": u"西甲深呼吸", "name": "none", "icon": "detail/5_fo.png"},
                {"label": u"西甲世界", "name": "none", "icon": "detail/4_fo.png"},
                {"label": u"情迷斗牛士", "name": "none", "icon": "detail/5_fo.png"},
                {"label": u"西甲塔帕斯", "name": "none", "icon": "detail/5_fo.png"},
                {"label": u"足彩大富翁", "name": "none", "icon": "detail/5_fo.png"},
                {"label": u"超级颜论", "name": "none", "icon": "detail/4_fo.png"},
                {"label": u"英超秀", "name": "none", "icon": "detail/4_fo.png"},
                {"label": u"十分英超", "name": "none", "icon": "detail/4_fo.png"}]
        elif channel == "wwe":
            listitems = [
                {"label": u"集锦", "name": "collection", "icon": "detail/2_fo.png"},
                {"label": u"赛事", "name": "schedule", "icon": "detail/2_fo.png"},
                {"label": u"TOP10", "name": "none", "icon": "detail/4_fo.png"}]
        elif channel == "ufc":
            listitems = [
                {"label": u"集锦", "name": "collection", "icon": "detail/2_fo.png"},
                {"label": u"赛事", "name": "schedule", "icon": "detail/2_fo.png"}]
        elif channel in ["suning", "im", "csl"]:
            listitems = [
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"}]
        elif channel == "cfa":
            listitems = [
                {"label": u"世预赛", "name": "collection", "icon": "detail/4_fo.png"}]
        elif channel in ["uefa", "afc", "cfacup", "nfl"]:
            listitems = [
                {"label": u"赛程", "name": "schedule", "icon": "detail/2_fo.png"},
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"}]
        elif channel == "bu":
            listitems = [
                {"label": u"赛程", "name": "schedule", "icon": "detail/2_fo.png"},
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"日尔曼锋火", "name": "none", "icon": "detail/5_fo.png"}]
        elif channel == "ere":
            listitems = [
                {"label": u"赛程", "name": "schedule", "icon": "detail/2_fo.png"},
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"绽放尼兰德", "name": "none", "icon": "detail/5_fo.png"}]
        elif channel == "ec":
            listitems = [
                {"label": u"赛程", "name": "schedule", "icon": "detail/2_fo.png"},
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"栏目", "name": "none", "icon": "detail/2_fo.png"}]
        elif channel == "cba":
            listitems = [
                {"label": u"资讯", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"赛程", "name": "schedule", "icon": "detail/2_fo.png"}]
        elif channel in ["cbs", "copa"]:
            listitems = [
                {"label": u"赛程", "name": "schedule", "icon": "detail/2_fo.png"}]
        else:
            listitems = [
                {"label": u"斯诺克", "name": "info", "icon": "detail/4_fo.png"},
                {"label": u"网球", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"飞镖", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"赛车", "name": "info", "icon": "detail/2_fo.png"},
                {"label": u"棋牌", "name": "info", "icon": "detail/2_fo.png"},]
        return listitems

    def init_schedule_list(self, startDate, endDate, competitionId="22"):
        if competitionId == "0":
            competitionId = "22"
        data = LIBRARY.fetch_schedule_list(startDate, endDate, competitionId)
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
                            "MatchType": item['strMatchType'],
                            "MatchCode": "-"
                            }
                yield listitem

    def init_infomation_list(self):
        data = LIBRARY.fetch_sport_recommend()
        if data:
            count = 0
            for module in data:
                for item in module['items']:
                    detaildata = item['comm_item']
                    if not detaildata['item_type'] in ['album', 'topic', 'video']:
                        continue
                    listitem = {'Label': detaildata['title'],
                                'Title': self.TITLE.decode('utf8'),
                                'icon': detaildata['pic_660x496'],
                                'fanart': detaildata['pic_1920x1080'],
                                'image_s': detaildata['pic_496x722'],
                                'type': detaildata['item_type'],
                                'position': str(count + 1),
                                'cid': detaildata.get('item_id', '')}
                    yield listitem

    @ch.click(C_LIST_CATEGORY)
    def schedule_list_click(self):
        lastitem = self.getControl(C_LIST_CATEGORY).getListItem(self.last_pos)
        lastitem.setProperty("current", "0")
        self.last_pos = self.getControl(C_LIST_CATEGORY).getSelectedPosition()
        item = self.getControl(C_LIST_CATEGORY).getSelectedItem()
        self.window.setProperty("CurrentDate", item.getProperty("label"))
        item.setProperty("current", "1")
        ymd = item.getProperty("ymd")
        lists = self.init_schedule_list(ymd, ymd)
        self.set_container(C_LIST_SCHEDULE, lists)

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
