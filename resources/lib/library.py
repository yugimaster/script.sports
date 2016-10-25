#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from sports import EPGAPI
try:
    import StorageServer2
except:
    import storageserverdummy as StorageServer2
try:
    import simplejson
except:
    import json as simplejson
from Utils import *


class LibraryFunctions():

    storageStack = {}

    def __init__(self):
        pass

    def _get_data(self, data_type, key=None, time=5):
        if data_type in self.storageStack:
            cache = self.storageStack[data_type]
        else:
            cache = StorageServer2.TimedStorage(data_type, time)
            self.storageStack[data_type] = cache
        if key is None:
            key = data_type
        try:
            _data = cache[key]
            print "-------GOT CACHE--------TYPE:" + data_type + " KEY:" + str(key)
            return _data
        except:
            print "--Error--GOT CACHE--------TYPE:" + data_type + " KEY:" + str(key)
            return None

    def _set_data(self, data_type, data, key=None, time=5):
        if data_type in self.storageStack:
            cache = self.storageStack[data_type]
        else:
            cache = StorageServer2.TimedStorage(data_type, time)
            self.storageStack[data_type] = cache
        if key is None:
            key = data_type
        cache[key] = data

    def fetch_sport_recommend(self):
        data = EPGAPI.get_sport_recommend()
        data = simplejson.loads(data)
        result = None
        if "result" in data and data['result']['ret'] == 0 and len(data['data']['channel_contents']) > 0:
            result = data['data']['channel_contents'][0]['modules']
        return result

    def fetch_live_sport(self):
        now_time = time.time()
        start_time = str(now_time - 43200)
        end_time = str(now_time + 43200)
        data = EPGAPI.get_live_sport(start_time, end_time)
        data = simplejson.loads(data)
        if data and "result" in data and data["result"].get("ret") == 0:
            return data
        return None

    def fetch_schedule_list(self, startDate, endDate, competitionId="22"):
        data = EPGAPI.get_schedule_list(competitionId, startDate, endDate)
        data = simplejson.loads(data)
        result = None
        if "data" in data:
            result = data['data']['vecMatchScheduleInfo']
        return result

    def fetch_date_list(self, now_time):
        month_map = {"01": "Jan .",
                     "02": "Feb .",
                     "03": "Mar .",
                     "04": "Apr .",
                     "05": "May .",
                     "06": "Jun .",
                     "07": "Jul .",
                     "08": "Aug .",
                     "09": "Sep .",
                     "10": "Oct .",
                     "11": "Nov .",
                     "12": "Dec ."}
        weekday_map = {"1": u"周一",
                       "2": u"周二",
                       "3": u"周三",
                       "4": u"周四",
                       "5": u"周五",
                       "6": u"周六",
                       "0": u"周日"}
        for count in range(-6, 7):
            time = now_time + 86400 * count
            month = SecondtoMonth(time)
            day = SecondtoDay(time)
            weekday = SecondtoWeekday(time)
            if count == 0:
                str_weekday = u"今日"
                current_state = "1"
            else:
                str_weekday = weekday_map[weekday]
                current_state = "0"
            item = {"label": str_weekday,
                    "label2": day,
                    "month": month_map[month],
                    "ymd": SecondtoYMD(time),
                    "current": current_state}
            yield item

    def fetch_time_tab(self, now_time):
        month_map = {"01": "1",
                     "02": "2",
                     "03": "3",
                     "04": "4",
                     "05": "5",
                     "06": "6",
                     "07": "7",
                     "08": "8",
                     "09": "9",
                     "10": "10",
                     "11": "11",
                     "12": "12"}
        for count in range(-6, 7):
            time = now_time + 86400 * count
            month = SecondtoMonth(time)
            day = SecondtoDay(time)
            if count == 0:
                str_date = "今天"
                current_state = "1"
            else:
                str_date = month_map[month] + "月" + day + "日"
                current_state = "0"
            len_date = len(str_date)
            if len_date == 6:
                texture_url = "detail/2_fo.png"
            elif len_date == 9:
                texture_url = "detail/4_fo.png"
            elif len_date == 10:
                texture_url = "detail/5_fo.png"
            else:
                texture_url = "detail/label_fo.png"
            item = {"label": str_date.decode('utf8'),
                    "icon": texture_url,
                    "ymd": SecondtoYMD(time),
                    "current": current_state}
            yield item

    def fetch_match_time(self, now_time):
        weekday_map = {"1": "（星期一）",
                       "2": "（星期二）",
                       "3": "（星期三）",
                       "4": "（星期四）",
                       "5": "（星期五）",
                       "6": "（星期六）",
                       "0": "（星期日）"}
        for count in range(-6, 7):
            time = now_time + 86400 * count
            ymd = SecondtoYMD(time)
            md = ymd[5:7] + "." + ymd[8:10]
            weekday = SecondtoWeekday(time)
            if count == 0:
                str_weekday = "（今天）"
                current_state = "1"
            elif count == -1:
                str_weekday = "（昨天）"
                current_state = "0"
            elif count == 1:
                str_weekday = "（明天）"
                current_state = "0"
            else:
                str_weekday = weekday_map[weekday]
                current_state = "0"
            item = {"label": (md + str_weekday).decode('utf8'),
                    "ymd": SecondtoYMD(time),
                    "current": current_state}
            yield item
