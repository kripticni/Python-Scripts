import requests

try:
    r = requests.get('https://httpbin.org/delay/6', timeout=3)
    print(r)
except:
    print('timeout')

print("="*75)

try:
    r = requests.get('https://httpbin.org/delay/3', timeout=6)
    print(r.content)
    print(r.text)
except:
    print('timeout')
    exit()
