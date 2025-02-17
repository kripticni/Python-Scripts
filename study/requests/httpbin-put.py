import requests

payload = {'username' : 'host' , 'password' : 'passwd'}
r = requests.put('https://httpbin.org/put', data = payload)

print(r.headers)
print(r.text)

print('='*75 + '\n' + str(r.json()))
