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

normale_toegangsprijs = 12.50
kortings_percentages = { "baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30 }
leeftijd = { "baby": (0,2), "kinderen": (3,18), "volwassenen": (19,64), "ouderen": (65,150) }

leeftijd_bezoeker = int(input("Geef uw leeftijd in aantal jaar: "))

for groep, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_bezoeker <= max_leeftijd:
        korting = kortings_percentages[groep]
        te_betalen = normale_toegangsprijs * (1 - korting / 100)
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {te_betalen:.2f}")
        break