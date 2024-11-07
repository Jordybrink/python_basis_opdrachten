# Opdracht 095_2
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

from my_modules import csv

data = [
    ['Naam', 'Leeftijd', 'Woonplaats'],
    ['Jordy', 34, 'IJsselmuiden'],
    ['Jeanine', 27, 'Zwolle'],
    ['Elina', 2, 'Genemuiden']
]

csv.schrijf_csv('gegevens.csv', data)
print("De gegevens zijn succesvol opgeslagen in 'gegevens.csv'")