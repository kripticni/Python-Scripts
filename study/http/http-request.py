import http.client

serv = http.client.HTTPConnection("httpbin.org")
serv.request("GET","/get")
response = serv.getresponse()
print(response.status)
print(response.reason)
print(response.read().decode())

data = response.read().decode()
print(data)

serv.request("GET","/a") 
response = serv.getresponse()
print(response.status)
print(response.reason)

serv.close()
#i think ill stick to the requests lib, or httpx
