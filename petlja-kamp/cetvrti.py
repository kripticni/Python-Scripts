n = int(input("Unesi broj upita: "))

vremena = []

for i in range(n):
    unos = input("Unesite vreme u formatu [0-23]:[0-59]:[0-59]  ")
    sati, minuti, sekunde = map(int, unos.split(":"))
    vremena.append((sati, minuti, sekunde))

for sati, minuti, sekunde in vremena:
    if sati < 9:
        sati = 24 + (sati - 9)
    else:
        sati -= 9

    print(f"{sati:02}:{minuti:02}:{sekunde:02}")
