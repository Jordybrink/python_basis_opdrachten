# Opdracht #060_1
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

my_list = []
for i in range(1, 11):
    my_list.append(i)
print(my_list)
