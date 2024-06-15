cena = int(input("Cena proizvoda je: "))
uplata = int(input("Uplata je: "))  # 1, 2 ,5 ,10 ,20 ,50 ,100

jedan = 0
dva = 0
pet = 0
deset = 0
dvadeset = 0
pedeset = 0
sto = 0

kusur = uplata - cena

while kusur >= 100:
    sto = sto+1
    kusur = kusur-100

while kusur >= 50:
    pedeset = pedeset+1
    kusur = kusur-50

while kusur >= 20:
    dvadeset = dvadeset+1
    kusur = kusur-20

while kusur >= 10:
    deset = deset+1
    kusur = kusur-10

while kusur >= 5:
    pet = pet+1
    kusur = kusur-5

while kusur >= 2:
    dva = dva+1
    kusur = kusur-2

while kusur > 0:
    jedan = jedan+1
    kusur = kusur-1

print(jedan)
print(dva)
print(pet)
print(deset)
print(dvadeset)
print(pedeset)
print(sto)
