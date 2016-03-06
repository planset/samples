#! /bin/usr/env python
# -*- coding:utf-8 -*-
"""
 `urllib2を使ってPOST,GETを投げてみよう｜Python <http://ameblo.jp/purigen/entry-10143483598.html>`_
"""
import urllib
import urllib2 #urllib2をインポートする

reqdata = {}
reqdata['q'] = 'python'
reqdata['lr'] = 'lang_ja'
reqdata['ie'] = 'utf-8'
reqdata['oe'] = 'utf-8'
reqdata['aq'] = 't'
reqdata['rls'] = 'org.mozilla:ja:official'
reqdata['client'] = 'firefox-a'

params = urllib.urlencode(reqdata)

#クライアントを作成
opener = urllib2.build_opener()

#User AgentをMozillaに変更(User-AgentがPython-urllib/*.*となっているので、Mozillaに変更)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.0.1)')]

#urllib.urlopen('http://www.google.co.jp/search?' + params)
#↑を作成したopenerを使ってopenするように変更
opener.open(url + params) #受信したHTMLを表示したい場合はopener.open(url + params).read().decode('utf-8')

