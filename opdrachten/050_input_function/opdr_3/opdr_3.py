# Opdracht 050_3
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

user_input = input("Vul hier je lijst in: ")
object_list = [item.strip() for item in user_input.split(",")]
sorted_list = sorted(object_list, reverse=True)
print(sorted_list)
