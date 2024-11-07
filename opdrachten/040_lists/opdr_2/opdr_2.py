# Opdracht 040_2
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

rivier_info = {"rijn": ["nederland", "duitsland", "Frankrijk"], "maas": ["nederland", "belgië", "duitsland"],"nijl": ["egypte", "soedan", "oeganda"]}
rivieren = list(rivier_info.keys())

print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[1]][0].capitalize()}")
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[2]][2].capitalize()}")
