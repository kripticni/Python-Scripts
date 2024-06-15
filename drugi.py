n = int(input("Unesite broj stanovnika: "))

lista = []

for i in range(n):
    godine = int(input("Unesite godine stanovnika: "))
    lista.append(godine)

max = -1
prosli = -1
index_max = -1
index_prosli = -1

for i, godine in enumerate(lista):
    if godine > max:
        prosli = max
        index_prosli = index_max
        max = godine
        index_max = i
    elif godine > prosli and godine < max:
        prosli = godine
        index_prosli = i

print("Drugi najstariji je", prosli, "i nalazi se na", index_prosli + 1, "-om mestu.")
