#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
`python :: urllib2 でhttps通信したときのめも - ichirin2501の日記 <http://d.hatena.ne.jp/ichirin2501/20110428/1303924574>`_
'''
import urllib
import urllib2
import cookielib

# http is urllib2.HTTPHandler(debuglevel=1)
opener = urllib2.build_opener(urllib2.HTTPSHandler(debuglevel=1),
                              urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
urllib2.install_opener(opener)

# https post
url = 'https://www.hatena.ne.jp/login'
login_post = {'name':'ichirin2501', 'password':'******'}
param = urllib.urlencode(login_post)
header = {
    'User-Agent' : 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16'
}
req = urllib2.Request(url, param, header)
res = urllib2.urlopen(req)

