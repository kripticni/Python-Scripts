import requests
r = requests.get('https://xkcd.com/353/')
print(r.text)

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.headers)
print('status code:', r.status_code)
print('is OK?', r.ok)

f = open('comic.png','wb')
f.write(r.content)

f.close()
