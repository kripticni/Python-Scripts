import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#making it not care about invalid ssl certs
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

s_url = input('url - ')
urls = [s_url]


while len(urls) > 0:
    url = urls.pop()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        link = tag.get('href', None)
        if link is not None and len(link) > 1:
            print(link)
            if link.startswith('http'):
                urls.append(link)
