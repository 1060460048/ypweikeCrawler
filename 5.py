# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re 
import webbrowser

#模拟登录一品威客网
class YiPin:
    #初始化方法
    def __init__(self):
#登录的URL地址
    self.loginURL = "http://www.epweike.com/login.html"
#代理ip地址，防止自己ip被封掉
    self.proxyURL = ''
#登录POST数据时发送的头部信息
    self.loginHeaders = {
            'Host':'www.epweike.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
            'Referer': 'http://www.epweike.com/',
            'Content-Type': 'text/html; charset=utf-8'
    }
