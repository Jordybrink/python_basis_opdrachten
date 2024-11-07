# Opdracht 060_2
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
result = [x * 3 for x in range(1, 21)][:6]
print(result)
