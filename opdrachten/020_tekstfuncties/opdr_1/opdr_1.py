# Opdracht 020_1
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

print("O mamma mia, wat maak je toch heerlijke pizza's")

fname = "Albert"
lname = "Einstein"
fullname = f"{fname} {lname} zei ooit:\'Als je niks fout doet, dan kun je ook niks leren!'"
print(fullname)