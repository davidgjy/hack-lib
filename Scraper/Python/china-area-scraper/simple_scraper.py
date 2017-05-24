import os
import pymysql
import time
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlretrieve
from urllib.request import urlopen

conn = pymysql.connect(host='localhost', user='root', passwd='mysql', db='mysql', port=3306, charset='utf8')
cur = conn.cursor()
cur.execute("USE scraper")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

url = "http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html"

req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)') 
response = urllib.request.urlopen(req)  
html = response.read()

bsObj = BeautifulSoup(html, "html.parser")
areaList = bsObj.findAll("p", {"class":"MsoNormal"})
level = 0
#chapter_content = bsObj.find("div", id="charpter_content")
for i in range(len(areaList)):
	codeNameTupple = areaList[i].get_text()
	if (is_number(codeNameTupple[0])):
		level = 1
	else:
		level = 2
	codeNameTupple = codeNameTupple.strip()
	code = codeNameTupple[0:6]
	name = codeNameTupple[6:].strip()
	print("code: %s" % code)
	print("name: %s" % name)
	print("level: %s" % level)
	#print("Html: %s" % name)
	#spanTupple = areaList[i].findAll("span")
	#print("代码: %s" % spanTupple[1].get_text())
	#print("名称: %s" % spanTupple[2].get_text())
	print("---------------------------------------")





