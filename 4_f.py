"""A csoport
Szimuláljuk egy 20 oldalú D&D kocka 100 db dobását! A dobásokat egy listában tároljuk! Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 6-os a dobások között?
2. Hányadikra sikerült először 18-nál nagyobbat dobni?
3. Hány darab 1-est dobtak?
4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
5. Mennyi a 4-es dobások szorzata?
"""
import random

dice_rolls = [random.randint (1, 20) for roll in range (100)]

print("4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?")
under_10 = [(value, idx) for idx, value in enumerate(dice_rolls) if value < 10]
if under_10:
    max_under_10 = max(under_10, key=lambda x: x[0])
    print(f"A legnagyobb dobás a 10-nél kisebbek közül: {max_under_10[0]} (ami a(z) {max_under_10[1] + 1}. dobás volt).")
else:
    print("Nem volt 10-nél kisebb dobás.")

print(f"A dobott számok: {dice_rolls}")