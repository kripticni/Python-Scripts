import requests
import urllib.parse
from bs4 import BeautifulSoup

visited = set()
rec = 0

def spider_url(url, keyword):
    global rec
    #print(f"recursion: {rec} : {url}")
    rec += 1
    
    if url in visited:
        return

    visited.add(url)

    try:
        response = requests.get(url, timeout=5)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tags = soup.find_all('a')
        href = []
        for tag in a_tags:
            link = tag.get('href',None)
            if link is not None and link != '':
                href.append(link)
        
        for link in href:
            link = urllib.parse.urljoin(url,link)
            if link in visited:
                continue
            visited.add(link)

            if keyword in link:
                print(link)
            
            spider_url(link, keyword)


url = input('url - ')
keyword = input('Keyword to search for in the url: ')
spider_url(url, keyword)
