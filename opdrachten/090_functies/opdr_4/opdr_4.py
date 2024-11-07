# Opdracht 090_4
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

def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        if naam['tussenvoegsel']:
            print(f"{naam['voornaam']} {naam['tussenvoegsel']} {naam['achternaam']}")
        else:
            print(f"{naam['voornaam']} {naam['achternaam']}")
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]
volledige_naam(namen)
