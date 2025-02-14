import requests

payload = {'username' : 'host' , 'password' : 'passwd'}
r = requests.post('https://httpbin.org/post', data = payload)

print(r.headers)
print(r.text)

print('='*75 + '\n' + str(r.json()))
