# Opdracht
# Student: Jordy Brink
# St.nummer: 98104602
# Groep:4ITX7

import os
from datetime import datetime
def cls():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
cls()

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

antwoorden = []
for vraag in vragen:
    antwoord = input(f"{vraag}\n")
    antwoorden.append(antwoord)
bestand_naam = "Results_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
with open(bestand_naam, "w") as file:
    file.write("Results\n")
    file.write("====================\n")
    for i in range(len(vragen)):
        file.write(f"{vragen[i]}\n{antwoorden[i]}\n\n")
print(f"De antwoorden zijn opgeslagen in {bestand_naam}")
