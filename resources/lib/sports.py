#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import urllib
import urllib2
import json
import xml.dom.minidom
import hashlib
from traceback import print_exc
from Utils import *
try:
    import simplejson
except:
    import json as simplejson


def make_qs(**params):
    return urllib.urlencode(params)


def GetHttpData(url, data=None, cookie=None, headers=None):
    xbmc.log("Fetch URL :%s, with data: %s" % (url, data))
    try:
        req = urllib2.Request(url)
        if cookie is not None:
            req.add_header('Cookie', cookie)
        if headers is not None:
            for headers in headers:
                req.add_header(headers, headers[headers])
        if data:
            response = urllib2.urlopen(req, data, timeout=3)
        else:
            response = urllib2.urlopen(req, timeout=3)
        httpdata = response.read()
        response.close()
    except urllib2.URLError, e:
        xbmc.log("URLError: " + str(e.reason))
        if str(e.reason) == 'getaddrinfo returns an empty list':
            httpdata = '{"status": "networkoff"}'
        elif str(e.reason) == '[Errno 11001] getaddrinfo failed':
            httpdata = '{"status": "networkoff"}'
        else:
            httpdata = '{"status": "Fail"}'
    except:
        print_exc()
        httpdata = '{"status": "Fail"}'
    return httpdata


class SoapClient():
    XML_TMPL = '''
<?xml version='1.0' encoding='utf-8'?>
 <SOAP-ENV:Envelope xmlns:SOAP-ENV="default" SOAP-ENV:encodingStyle="default">
   <SOAP-ENV:Body>
        <{method} {params} />
    </SOAP-ENV:Body>
 </SOAP-ENV:Envelope>'''

    def __init__(self):
        pass

    def request(self, location, xml):
        headers = {'Content-Type': "application/xml"}
        req = urllib2.Request(location, xml, headers)
        try:
            return urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            code = e.code
            return str(code)

    def __getattr__(self, attr):
        return lambda **kwargs: self.call(attr, **kwargs)

    def call(self, api, method, **params):
        self._build_xml(method, **params)
        response = self.request(api, self.xml_request)
        if type(response) == str:
            headers = response
            body = ""
            return headers, body
        content = response.read()
        body = ""
        if len(content) > 0:
            body = self.load_xml(content)
        return response.headers, body

    def load_xml(self, text):
        document = xml.dom.minidom.parseString(text)
        root = document.documentElement
        body = root.getElementsByTagName("SOAP-ENV:Body")[0]
        return body

    def _build_xml(self, method, **params):
        _params = " ".join('%s="%s"' % (key, params[key]) for key in params)
        self.xml_request = self.XML_TMPL.format(method=method, params=_params)


class OISAPI():

    def __init__(self):
        self.client = SoapClient()


class EPGAPI(object):

    API = "http://tv.t002.ottcn.com/i-tvbin/qtv_video/"
    LICENSE = "icntv"
    QUA = "&Q-UA=QV%3D1%26VN%3D1.1.27%26PT%3DPVS%26RL%3D1920x1080%26IT%3D12117592000%26OS%3D1.1.27%26CHID%3D13033%26DV%3Dtencent_macaroni"

    @classmethod
    def get_sport_recommend(self):
        """get sport recommend
        """
        return GetHttpData(self.API + 'home_page/get_home_page?tv_cgi_ver=1.0&format=json&req_from=PVS_APK&req_type=get&channel_selector=specify&channel_ids=physical_pay&content_selector=all' + self.QUA)

    @classmethod  # sport recommend
    def get_live_sport(self, start, end):
        """get live sport
        """
        return GetHttpData(self.API + 'live_details/get_live_schedule?req_from=PVS_APK&site_selector=sports&live_status_filter=1,2,3&pay_selector=0,1&format=json&start_time={0}&end_time={1}'.format(start, end) + self.QUA)

    @classmethod  # schedule
    def get_schedule_list(self, startDate, endDate):
        """get schedule list
        """
        return GetHttpData(self.API + 'match/get_match_list?competitionId=22&startTime={0}&endTime={1}&version=1&format=json&licence={2}'.format(startDate, endDate, self.LICENSE))

    def _get(self, API, **param):
        data = QueryParams(API, **param)
        data = GetHttpData(self.SERVER + API + "?" + urllib.urlencode(data))
        s = simplejson.loads(data)
        xbmc.log(json.dumps(s, sort_keys=True,
                 indent=4, separators=(',', ': ')))
        try:
            return s
        except:
            return None

    def _post(self, API, **param):
        data = QueryParams(API, **param)
        data = GetHttpData(self.SERVER + API, urllib.urlencode(data), headers=data)
        try:
            return simplejson.loads(data)
        except:
            return None


class QueryParams(dict):
    BASE_PARA = {"token": "guoziyun"}

    def __init__(self, API, **arg):
        self._update(self.BASE_PARA)
        self._update(arg)
        self._sign(API)

    def _update(self, dict):
        for k, v in dict.items():
            self[k] = v

    def _sign(self, API):
        preurl = API + "?"
        od = [(k, self[k]) for k in sorted(self.keys())]
        preurl += urllib.urlencode(od, True)
        m = hashlib.md5()
        m.update(preurl)
