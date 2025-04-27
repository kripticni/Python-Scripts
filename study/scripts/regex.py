import re

text = open('text.txt','r')

for line in text:
    if re.search('^py', line):
        print(line)

#for line in text:
#    if re.search('py', line):
#    #if line.find('py') >= 0:
#        print(line)

text.close()
text = open('text.txt','r')
matching = re.findall('^py.*', text.read(), re.MULTILINE)
print(matching)

#performs exactly the same at this size
