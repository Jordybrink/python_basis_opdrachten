# Opdracht 020_1
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

# Hier komt je code...

# Opdracht 1a
# Zorg dat de volgende zin op het scherm wordt getoond met de print-functie:
# O mamma mia, wat maak je toch heerlijke pizza's
print("O mamma mia, wat maak je toch heerlijke pizza's")

# Gebruik onderstaande variabelen en de print-functie
# en toon de volgende zin op het scherm: Albert Einstein zei ooit: 'Als je niks fout doet, dan kun je ook niks leren!'
fname = "Albert"
lname = "Einstein"
fullname = f"{fname} {lname} zei ooit:\'Als je niks fout doet, dan kun je ook niks leren!'"
print(fullname)