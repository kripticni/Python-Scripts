#same mechanics as cpp
months = {
    "jan" : "January",
    "feb" : "February",
    "mar" : "March",
}

print(months["Jan".lower()])
print(months.get("Feb".lower()))
print(months.get("false".lower()))
print(months.get("false".lower(), "not existing, resorts to this default"))

x = {1,2,3,4,5}
y = 0

graph = dict.fromkeys(x,y) #so this is a static function
graph.popitem()
graph.setdefault(1,1)
print(graph.items())
