# Opdracht 080_2
# Student: Jordy Brink
# St.nummer: 98104602
# Groep:4ITX7

import random
import os
def cls():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
cls()

geheim_getal = random.randint(1, 100)

pogingen = 0

print("Raad mijn geheime getal")

while True:
    try:
        gok = int(input("Raad mijn geheime getal: "))
    except ValueError:
        print("Voer een geldig getal in!")
        continue
    pogingen += 1
    if gok < geheim_getal:
        print("Hoger!")
    elif gok > geheim_getal:
        print("Lager!")
    else:
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {pogingen} keer gedaan.")
        break
