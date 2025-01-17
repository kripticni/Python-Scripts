#pretty similar to C++
string = input()

#since py is OOP, there is operator
#overrides and plenty of methods

print("The input is %s" %str(string))
print("Length of input is %i" %len(string))
print("%s in uppercase" %string.upper())
print("%s in lowercase" %string.lower())
print("%s in switched cases" %string.swapcase())
print("%s in title cases" %string.title())
print("is %s lowercase? %s" %(str(string), string.islower()))
print("is %s uppercase? %s" %(str(string), string.isupper()))
print("does %s start with 'a'? %s" %(str(string), string.startswith('a')))
print("does %s end with 'a'? %s" %(str(string), string.endswith('a')))
print("first 'a' in input is at position", string.index('a'))
print("count of 'a's in input ", string.count('a'))
print("'a's replaced with 'b's ", string.replace("a","b"))
print("encoded string ", string.encode())
print("stripped string ", string.strip())

print("characters in input by index")
for i in range(0, len(string)):
    print(i, string[i])
