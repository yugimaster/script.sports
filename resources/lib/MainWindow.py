# -*- coding: utf-8 -*-

import xbmcgui
import time
from BaseClasses import *
from dialogs.DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
from library import LibraryFunctions
from Utils import *
from WindowManager import wm

ch = OnClickHandler()
LIBRARY = LibraryFunctions()
C_ITEM_RECOMMEND = 9000
C_LIST_REVIEW = 9001
C_LIST_RECOMMEND_ONE = 9002
C_LIST_RECOMMEND_TWO = 9003
C_LIST_RECOMMEND_THREE = 9004
C_LIST_RELATE = 9005
C_LIST_MATCH = 9006
C_LIST_DATE = 9007
C_LIST_SCHEDULE = 9008


class MainWin(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)
        self.DATA = None
        self.last_pos = 6

    def onInit(self):
        self.window_id = xbmcgui.getCurrentWindowId()
        self.window = xbmcgui.Window(self.window_id)
        self.set_recommend_list()
        self.set_relate_list()
        self.set_sport_match()
        self.set_schedule_table()

    def set_recommend_list(self):
        lists = self.init_recommend_list()
        if lists:
            total = len(lists)
            if total < 1:
                return
            review_hot = lists[:1]
            self.set_container(C_ITEM_RECOMMEND, review_hot, True)
            if total < 2:
                return
            recommend_list_one = lists[1:3]
            self.set_container(C_LIST_RECOMMEND_ONE, recommend_list_one)
            if total < 4:
                return
            recommend_list_two = lists[3:5]
            self.set_container(C_LIST_RECOMMEND_TWO, recommend_list_two)
            if total < 6:
                return
            recommend_list_three = lists[5:6]
            self.set_container(C_LIST_RECOMMEND_THREE, recommend_list_three)
            if total > 6:
                review_list = lists[6:]
                self.set_container(C_LIST_REVIEW, review_list)

    def set_relate_list(self):
        lists = self.init_relate_list()
        self.set_container(C_LIST_RELATE, lists)

    def set_sport_match(self):
        lists = self.init_sport_match()
        self.set_container(C_LIST_MATCH, lists)

    def set_schedule_table(self):
        now_time = time.time()
        ymd = SecondtoYMD(now_time)
        date_list = self.init_date_list(now_time)
        self.set_container(C_LIST_DATE, date_list)
        self.getControl(C_LIST_DATE).selectItem(6)
        schedule_list = self.init_schedule_list(ymd, ymd)
        self.set_container(C_LIST_SCHEDULE, schedule_list)

    def init_relate_list(self):
        item = {
            "label": u"西 甲",
            "image": "home/relate_list/LaLiga.png",
            "icon": "home/relate_list/LaLiga_fo.png",
            "name": "laliga",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"英 超",
            "image": "home/relate_list/PL.png",
            "icon": "home/relate_list/PL_fo.png",
            "name": "pl",
            "competitionId": "8"
        }
        yield item
        item = {
            "label": u"栏目",
            "image": "home/relate_list/FN.png",
            "icon": "home/relate_list/FN_fo.png",
            "name": "column",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": "WWE",
            "image": "home/relate_list/WWE.png",
            "icon": "home/relate_list/WWE_fo.png",
            "name": "wwe",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": "UFC",
            "image": "home/relate_list/UFC.png",
            "icon": "home/relate_list/UFC_fo.png",
            "name": "ufc",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"苏宁专区",
            "image": "home/relate_list/SN.png",
            "icon": "home/relate_list/SN_fo.png",
            "name": "suning",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"国米专区",
            "image": "home/relate_list/IM.png",
            "icon": "home/relate_list/IM_fo.png",
            "name": "im",
            "competitionId": "0"
        }
        yield item

    def init_sport_match(self):
        item = {
            "label": u"中国之队",
            "image": "home/sport_match/CFA.png",
            "icon": "home/sport_match/CFA_fo.png",
            "name": "cfa",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"欧 冠",
            "image": "home/sport_match/UEFA.png",
            "icon": "home/sport_match/UEFA_fo.png",
            "name": "uefa",
            "competitionId": "5"
        }
        yield item
        item = {
            "label": u"德 甲",
            "image": "home/sport_match/Bundesliga.png",
            "icon": "home/sport_match/Bundesliga_fo.png",
            "name": "bu",
            "competitionId": "22"
        }
        yield item
        item = {
            "label": u"亚 冠",
            "image": "home/sport_match/AFC.png",
            "icon": "home/sport_match/AFC_fo.png",
            "name": "afc",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"足协杯",
            "image": "home/sport_match/CFA-CUP.png",
            "icon": "home/sport_match/CFA-CUP_fo.png",
            "name": "cfacup",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"荷 甲",
            "image": "home/sport_match/Eredivisie.png",
            "icon": "home/sport_match/Eredivisie_fo.png",
            "name": "ere",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"俄 超",
            "image": "home/sport_match/2001.png",
            "icon": "home/sport_match/2001_fo.png",
            "name": "po",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": "NFL",
            "image": "home/sport_match/NFL.png",
            "icon": "home/sport_match/NFL_fo.png",
            "name": "nfl",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"中 超",
            "image": "home/sport_match/CSL.png",
            "icon": "home/sport_match/CSL_fo.png",
            "name": "csl",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": "CBA",
            "image": "home/sport_match/CBA.png",
            "icon": "home/sport_match/CBA_fo.png",
            "name": "cba",
            "competitionId": "100008"
        }
        yield item
        item = {
            "label": u"巴 甲",
            "image": "home/sport_match/CBS.png",
            "icon": "home/sport_match/CBS_fo.png",
            "name": "cbs",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": "FA CUP",
            "image": "home/sport_match/FACUP.png",
            "icon": "home/sport_match/FACUP_fo.png",
            "name": "facup",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"解放者杯",
            "image": "home/sport_match/COPA.png",
            "icon": "home/sport_match/COPA_fo.png",
            "name": "copa",
            "competitionId": "0"
        }
        yield item
        item = {
            "label": u"更 多",
            "image": "home/sport_match/more.png",
            "icon": "home/sport_match/more_fo.png",
            "name": "more",
            "competitionId": "more"
        }
        yield item

    def init_recommend_list(self):
        listitems = []
        if not self.DATA:
            self.DATA = LIBRARY.fetch_sport_recommend()
            data = self.DATA
            if data:
                count = 0
                for module in data:
                    for item in module['items']:
                        detaildata = item['comm_item']
                        if not detaildata['item_type'] in ['album', 'topic', 'video']:
                            continue
                        listitem = {'Label': detaildata['title'],
                                    'Title': detaildata['title'],
                                    'icon': detaildata['pic_660x496'],
                                    'fanart': detaildata['pic_1920x1080'],
                                    'image_s': detaildata['pic_496x722'],
                                    'type': detaildata['item_type'],
                                    'position': str(count + 1),
                                    'cid': detaildata.get('item_id', '')}
                        listitems.append(listitem)
                        count += 1
        return listitems

    def init_date_list(self, time):
        return LIBRARY.fetch_date_list(time)

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

    def onAction(self, action):
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(MainWin, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(C_LIST_DATE)
    def schedule_list_click(self):
        wm.open_schedule_detail_window()

    @ch.click([C_LIST_RELATE, C_LIST_MATCH])
    def open_match_window(self):
        control_id = self.getFocusId()
        item = self.getControl(control_id).getSelectedItem()
        competitionId = item.getProperty("competitionId")
        match_name = item.getProperty("label")
        channel = item.getProperty("name")
        wm.open_match_schedule_window(match_name.replace(" ", ""), channel, competitionId)

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
