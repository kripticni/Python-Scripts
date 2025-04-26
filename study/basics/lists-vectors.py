#lists in python are actually standard vectors
lista = [1, 2, 3, 4, 5]
save = lista.copy()

print(lista)
lista.sort()
print(lista)
lista = save.copy()
lista.reverse()
print(lista)
lista = save.copy()
lista.remove(1)
print(lista)
lista = save.copy()
ans = lista.pop(2)
print(lista, ans)
lista.clear()
print(lista)
