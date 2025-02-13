import requests

# error prone way, requests lib offers a better solution
r = requests.get('https://httpbin.org/get?page=2&count=25')

payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params = payload)

print(r.headers)
print(r.text)
