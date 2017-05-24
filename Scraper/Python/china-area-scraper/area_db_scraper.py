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

def clearTable():
    sql = "truncate table areas"
    cur.execute(sql)
    cur.connection.commit()
    print("****** Table is clear now!! ******")

def storeArea(name, code, level):
    sql = "INSERT INTO areas(name, code, level, create_time) VALUES (%s, %s, %s, Now())"
    cur.execute(sql, (name, code, level))
    cur.connection.commit()
    print("****** 区域: %s has been saved to database! ******" % (name));

clearTable()
url = "http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)') 
response = urllib.request.urlopen(req)  
html = response.read()

bsObj = BeautifulSoup(html, "html.parser")
areaList = bsObj.findAll("p", {"class":"MsoNormal"})
level = 0
#chapter_content = bsObj.find("div", id="charpter_content")
count = 0
for i in range(len(areaList)):
    codeNameTupple = areaList[i].get_text()
    
    if (is_number(codeNameTupple[0])):
        level = 1
    else:
        if (codeNameTupple[0:2] == "\u3000\u3000"):
            level = 3
        else:
            level = 2
    
    if (codeNameTupple[15:21].strip() != "市辖区"):
        codeNameTupple = codeNameTupple.strip()
        code = codeNameTupple[0:6]
        name = codeNameTupple[6:].strip()
        print("code: %s" % code)
        print("name: %s" % name)
        print("level: %s" % level)
        storeArea(name, code, level)
        print("---------------------------------------------")        
    else:
        count = count + 1
        print("排除第%d个[市辖区]" % count)
        print("---------------------------------------------")  
    
