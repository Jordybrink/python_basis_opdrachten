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

y_values = [4*x + 7 for x in range(1, 10)]
print(y_values)
