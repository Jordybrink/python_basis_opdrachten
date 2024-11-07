# Opdracht 050_2
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

gasten = ["Jordy", "Paul", "Kees", "Marie", "Hilda"]

print("Lijst met gasten:", gasten)
gasten.remove("Marie")

print("Marie heeft afgezegd:", gasten)
index_van_kees = gasten.index("Kees")
gasten.insert(index_van_kees + 1, "George")

print(f"George wil ook mee: {gasten}")
print()