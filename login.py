# -*- coding: utf-8 -*-


import ssl
import urllib2
from cookielib import CookieJar


context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
# print urllib2.urlopen("https://test-hcz-member.pingan.com.cn:8143/login/user/sms/login", context=context).read()

loginUrl = 'https://test-hcz-member.pingan.com.cn:8143/login/user/sms/login '
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'hczandroid/3.15.1/6.0',
    'Host': 'test-hcz-member.pingan.com.cn:8143',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Content-Length': '111',
    }
loginData = 'dynamicCode=1708&mobilePhone=18600010003&imageCode=&equipmentNo=3f1d7a98653fbc5a75aabdcd5ea1e172d&phoneOsType=2'
cookieJar = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
handler = urllib2.urlopen("https://test-hcz-member.pingan.com.cn:8143/login/user/sms/login", context=context)
req = urllib2.Request(loginUrl, loginData, headers)
loginResult = opener.open(req).read()
print loginResult
