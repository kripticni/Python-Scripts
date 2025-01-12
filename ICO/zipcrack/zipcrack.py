import zipfile

filename = input("Input the name of the zip: ")
wordlist = input("Input the name of the wordlist: ")

try:
    zipf = zipfile.ZipFile(filename)
except FileNotFoundError:
    print("file ", filename, " not found")
    exit()

try:
    plist = open(wordlist, "r")
except FileNotFoundError:
    print("file ", wordlist, " not found")
    exit()

cracked = False

for line in plist:
    try:
        zipf.extractall("output", pwd=line.strip().encode())
        cracked = True
        exit()
    except RuntimeError:
        continue

if cracked == True:
    print("cracked")
else:
    print("not found")
