from urllib.parse import quote
from urllib.parse import urlencode
from urllib.parse import urlunparse
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import parse_qs
from urllib.parse import urlparse

path = 'pypi'
path_enc = quote(path)
query_dict = {':action': 'search', 'term': 'urlopen'}
query_enc = urlencode(query_dict)

netloc = 'pypi.python.org'
encodedUrl = urlunparse(('http', netloc, path_enc, '', query_enc, ''))
print('Request url: %s' % encodedUrl)
result = urlparse(encodedUrl)
content = parse_qs(result.query)
print('Content: %s' % content)
