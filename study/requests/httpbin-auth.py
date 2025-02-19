import requests

r = requests.get('https://httpbin.org/basic-auth/admin/passwd', auth=('admin','passwd'))

print("Method: ", r.request.method)
print("Url: ", r.request.url)
print("Headers: ", r.request.headers)
print("Headers: ", r.request.body)

print()

print(r.headers)
print(r.text)

