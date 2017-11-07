import urllib
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode

postdata = {"channelId": "", "couponName": "", "couponType": "", "merchantId": "", "pageNum": 1, "pageSize": 10, "token": "82ytauht9unsdnkyc7e91bf547011d4ae68d0de50014e6a7da1ddb2215fe8e3d983938654d453b1d"}
data = urllib.parse.urlencode(postdata).encode(encoding='UTF8')
req = Request("http://139.224.29.14:8085/yxc-hive/coupon/queryCouponMain",data=data)
req.add_header('Content-Type', 'application/json')
response = urlopen(req)

#print('Post Response: %s' % response.read())