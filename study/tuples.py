#tuples are immutable in python, which is weird
string = input("first: ")
integer = int(input("second: "))
float = float(input("third: "))

tuple = (string, integer, float)
print(tuple)

#list = [tuple]
list = [] #this is partially unknown type
for i in range(0,5):
    list.append(tuple)

print(list)
