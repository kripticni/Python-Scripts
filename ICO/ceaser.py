text = input()
key = int(input())

res = '';
ch = '';

for c in text:
    ch = chr((ord(c) - ord('a') + key) % 26 + ord('a'))
    res = res + ch;
    
print(res)
