from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

s_url = input('url - ')
visited = {s_url: False}
urls = [s_url]

while len(urls) > 0:
    url = urls.pop()
    if visited[url] is True:
        continue

    visited[url] = True
    fd = urllib.request.urlopen(url, context=ctx)
    html = fd.read()

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a')

    for tag in tags:
        link = tag.get('href', None)
        if link is None or len(link) < 2:
            continue

        link = urllib.parse.urljoin(url,link)

        if link.startswith('http') and link not in visited:
            urls.append(link)
            visited[link] = False

        print(link)
