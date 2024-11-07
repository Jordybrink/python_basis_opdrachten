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

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]
keuze = input(f"Kies je topping uit deze lijst: {beschikbare_toppings} ")

gezocht = None
for topping, prijs in toppings:
    if keuze.lower() == topping:
        gezocht = (topping, prijs)
        break

if gezocht:
    print(f"U heeft {gezocht[0]} besteld. Dat kost {gezocht[1]:.2f}")
else:
    print("Uw keuze zit niet in ons assortiment")