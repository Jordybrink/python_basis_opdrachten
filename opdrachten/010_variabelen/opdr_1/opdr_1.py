# Opdracht 010_1
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

my_list = [13, "wat een weertje", 12.5, 8]
for item in my_list:
    print(item)