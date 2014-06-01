#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import requests
from lxml import etree

class WebAPI(object):
    pass

class StatDB(WebAPI):
    def __init__(self, app_id, host, version, lang='J'):
        self.host = host
        self.version = version

        self.make_api_urls()

        self.lang = lang
        self.appId = app_id

    def make_api_urls(self):
        self.BASE_URL = 'http://{host}/api/{version}/app/'.format(
                host=self.host, version=self.version)
        self.STATS_URL = urlparse.urljoin(self.BASE_URL, 'getStatsList')
        self.META_URL = urlparse.urljoin(self.BASE_URL, 'getMetaInfo')
        self.DATA_URL = urlparse.urljoin(self.BASE_URL, 'getStatsData')
        self.DATA_SET_URL = urlparse.urljoin(self.BASE_URL, 'postDataset')
        self.DATA_SET_REF_URL = urlparse.urljoin(self.BASE_URL, 'refDataset')

    def stats_list(self):
        params = {
                'appId': self.appId,
                'lang': self.lang,
                'surveyYears': '2012'
                }
        res = requests.get(self.STATS_URL, params=params)
        root = etree.fromstring(res.content)
        datalist_inf = root.find('DATALIST_INF')
        number = datalist_inf.find('NUMBER')
        datalist = datalist_inf.findall('LIST_INF')
        print 'NUMBER:', number.text
        for data in datalist[:10]:
            print '='*80
            print data.find('STAT_NAME').text
            print data.find('GOV_ORG').text
            print data.find('STATISTICS_NAME').text
            print data.find('TITLE').text
            print data.find('CYCLE').text
            print data.find('SURVEY_DATE').text
            print data.find('OPEN_DATE').text
            print data.find('SMALL_AREA').text
            print 



app_id = '653d6f5dfe4f78475ad2609ca8063bfb29ac679a'
host = 'statdb.nstac.go.jp'
version = '1.0b'
sdb = StatDB(app_id, host, version)
print sdb.stats_list()



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
