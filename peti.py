n = int(input("Unesite broj dana: "))
cene = [int(input("Unesite cenu za dan: ")) for i in range(n)]

min_cena = 100000000
min_index = -1

for i in range(n - 6):
    trenutna_cena = sum(cene[i:i+7])
    if trenutna_cena < min_cena:
        min_cena = trenutna_cena
        min_index = i

print(min_index)
print(min_cena)
