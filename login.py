#!/usr/bin/python

import urllib  
import urllib2  
import cookielib  

#hosturl = 'http://10.104.0.225/forum.php?mod=viewthread&tid=323'

acturl = 'http://10.104.0.225/plugin.php?id=xj_event:event_userlist&tid=323'

posturl = 'http://10.104.0.225/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

h = urllib2.urlopen(hosturl) 
#print h
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36','Referer' : 'Referer: http://10.104.0.225/portal.php?mod=list&catid=3'}

postData = {'fastloginfield' : 'username',
            'username' : '用户名',
            'password' : '密码', 
            'quickforward' : 'yes',
            'handlekey' : 'ls'
            }
postData = urllib.urlencode(postData)  
  
cookieJar = cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))

req=urllib2.Request(posturl,postData,headers)
result=opener.open(req)
result=opener.open(acturl)
print result.read()
#h = urllib2.urlopen(hosturl,postData,headers) 
