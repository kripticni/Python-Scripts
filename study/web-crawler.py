import urllib.request, urllib.error, urllib.parse, re
from bs4 import BeautifulSoup

s_url = input('Site - ')
if(len(s_url) < 1):
   s_url = 'http://www.dr-chuck.com/page1.htm'

urls = [s_url]
while len(urls) > 0:
    url = urls.pop()
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        link = tag.get('href', None)
        if link is not None:
            print(link)
            if link.startswith('http'):
                urls.append(link)
