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

print("2. Hányadikra sikerült először 18-nál nagyobbat dobni?")
try:
    elso_18_felett = dice_rolls.index(next(filter(lambda x: x > 18, dice_rolls))) + 1
    print(f"Az első 18-nál nagyobb dobás a {elso_18_felett}. dobás volt.")
except StopIteration:
    print("Nem volt 18-nál nagyobb dobás.")

print(f"A dobott számok: {dice_rolls}")