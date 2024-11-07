# Opdracht 020_2
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

zin1 = "Tinus gaat op zijn tandem naar de hottentottententoonstelling"  
count_t = zin1.count('t')

print(f"De letter 't' komt {count_t} keer voor in de tekst.")