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

output = []
for i in range(3, 82, 3):  
    result = (i ** 2) / 3
    output.append(result)

print(output)
