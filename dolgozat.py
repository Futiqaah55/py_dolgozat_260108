#1. feladat:

ljegyek = [2, 2, 4, 5, 5, 3]


atlag = sum(ljegyek) / len(ljegyek)
print(f"Átlag: {atlag}")


if atlag % 1 == 0.5:
    valasz = input("Az átlag .5-re végződik. Szeretnél javítani? (i/n): ")

    if valasz.lower() == "i":
        javitas = int(input("Add meg a javítás eredményét: "))
        ljegyek.append(javitas)
        atlag = sum(ljegyek) / len(ljegyek)
        vegso_jegy = round(atlag)
    else:
        vegso_jegy = int(atlag)  # rosszabb jegy
else:
    vegso_jegy = round(atlag)

print(f"Félévkor kapott jegy: {vegso_jegy}")

#2. feladat:

Lkoltesek = ["1200", "1500", "0", "900", "1400", "3150", "0"]
koltesek = [int(x) for x in Lkoltesek]

napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

atlag = sum(koltesek) / len(koltesek)
print(f"Napi átlagos költés: {atlag} Ft")

db_2000_felett = 0
for k in koltesek:
    if k > 2000:
        db_2000_felett += 1
print(f"2000 Ft feletti költések száma: {db_2000_felett}")

max_koltes = max(koltesek)
index = koltesek.index(max_koltes)
print(f"A legtöbbet {napok[index]} költötte: {max_koltes} Ft")

zsebpenz = int(input("Add meg a kapott zsebpénzt (Ft): "))
maradek = zsebpenz - sum(koltesek)

if maradek > 0:
    print(f"Maradt pénz a következő hétre: {maradek} Ft")
elif maradek == 0:
    print("Pont elfogyott a zsebpénz.")
else:
    print(f"Nem volt elég a zsebpénz, hiány: {-maradek} Ft")

#3. feladat:
import random


homersekletek = [random.randint(-20, 40) for _ in range(12)]

honapok = [
    "Január", "Február", "Március", "Április",
    "Május", "Június", "Július", "Augusztus",
    "Szeptember", "Október", "November", "December"
]

print("Havi átlaghőmérsékletek:")
for i in range(12):
    print(f"{honapok[i]}: {homersekletek[i]} °C")

fagyos = 0
for h in homersekletek:
    if h < 0:
        fagyos += 1
print(f"\nFagyos hónapok száma: {fagyos}")

atlag = sum(homersekletek) / len(homersekletek)
print(f"Éves átlaghőmérséklet: {atlag:.2f} °C")

max_h = max(homersekletek)
min_h = min(homersekletek)

print(f"Legmelegebb hónap: {honapok[homersekletek.index(max_h)]} ({max_h} °C)")
print(f"Leghidegebb hónap: {honapok[homersekletek.index(min_h)]} ({min_h} °C)")

for i in range(12):
    if homersekletek[i] > 30:
        print(f"Hőség volt ebben a hónapban! ({honapok[i]})")
