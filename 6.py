# encoding:utf-8
import urllib, urllib2, cookielib, re
 
# 账号相关参数
username = '1060460048@qq.com'
#password = '112752zjy'
password = '0e0d25f9ad21e0eae09e2814736c2907'
login_type = 3
ckb_cookie = 0
hdn_refer = 'http://www.epweike.com/index.php'
txt_code = ''
pre = 'login'
inajax = 1
 
# cookie设置
cj = cookielib.CookieJar()
cookie_hanler = urllib2.HTTPCookieProcessor(cj)
 
# 获取once的值
lgurl = 'http://www.epweike.com/index.php'
req = urllib2.Request(url = lgurl)
opener = urllib2.build_opener(cookie_hanler)
urllib2.install_opener(opener)
contents = opener.open(req)
contents = contents.read()

# 根据正则表达式匹配once值
reg = r'name="formhash"(.*?) value="(.*)"'
pattern = re.compile(reg)
result = pattern.findall(contents)
 
# 登录参数设置
lgurl = 'http://www.epweike.com/index.php?do=login'
data = {'formhash':result[0][1], 'txt_account':username, 'pwd_password':password, 'login_type':login_type, 'ckb_cookie':ckb_cookie, 'hdn_refer':hdn_refer, 'txt_code':txt_code, 'pre':pre, 'inajax':inajax}
data = urllib.urlencode(data)
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Safari/537.36', 'Referer':'http://www.epweike.com/login.html', 'Host':'www.epweike.com'}
req = urllib2.Request(url = lgurl, data = data, headers = hdr)
opener = urllib2.build_opener(cookie_hanler)
 
# 进行登录操作
response = opener.open(req)
page = response.read()
#print(page)
 
# 可以随便访问其他的链接
contents = urllib2.urlopen('http://www.epweike.com/index.php?do=user&view=index')
contents = contents.read()
print(contents)
