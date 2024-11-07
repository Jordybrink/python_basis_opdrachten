# Opdracht
# Student: Jordy Brink
# St.nummer: 98104602
# Groep:4ITX7
import os
def cls():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
cls()

# Maak een lege lijst
getallen = []

# Gebruik een loop om de lijst te vullen met getallen van 1 t/m 10
for i in range(1, 11):
    getallen.append(i)

# Print alleen de getallen die groter zijn dan 4
for getal in getallen:
    if getal > 4:
        print(getal)
