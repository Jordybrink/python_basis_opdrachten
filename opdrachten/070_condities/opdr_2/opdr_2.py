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

getallen = [43948, 878768, 38768, 87555, 765765]

for getal in getallen:
    if getal % 3 == 0:
        print(getal)
