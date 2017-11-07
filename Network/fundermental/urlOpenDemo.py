import urllib.error
from urllib.request import urlopen
from urllib.request import Request

def getUrlResponse(url):
    try:
        req = Request(url)
        response = urlopen(req)
        content = response.read()
        print('Content: %s' % content)
        print(response.getheader('Content-Encoding'))
        contentType,charset = response.getheader('Content-Type').split(';')
        print('content type: %s' % contentType)
        print('charset: %s' % charset)
        agent = req.get_header('User-agent')
        print('User agent: %s' % agent)
        
    except urllib.error.HTTPError as e:
        print('status', e.code)
        print('reason', e.reason)
        print('url', e.url)

def main():
    url = 'http://www.baidu.com'
    getUrlResponse(url)
    
if __name__ == "__main__":
    main()
