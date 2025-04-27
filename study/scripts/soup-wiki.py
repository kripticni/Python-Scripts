import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fd = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python', context=ctx)
html = fd.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.find_all('span'))

