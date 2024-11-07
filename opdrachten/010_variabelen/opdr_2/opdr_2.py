# Opdracht 010_2
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

my_tuple = [11, "Oh een tuple", 13.5, 8009]
for item in my_tuple:
    print(item)