# Opdracht 020_3
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
Boom = ["       *     ", "      ***    ", "    ******   ", "   ********  ", " *********** ", "     ***     ", "     ***     ", "     ***     "] 
for item in Boom:
    print(item * 5)

'''
print("    *")
#print("   ***")
#print("  ******")
#print(" ********")
#print("***********")
#print("    ***")
#print("    ***")
#print("    ***")
# my_dict = ["naam = willem", "Achternaam = van der broek", "Leeftijd = 23", "Favoriete kleur = blauw",] 
# for item in my_dict:
#   print(item)
"    *", "   ***", "  ******", " ********", "***********", "    ***", "    ***", "    ***"
''' 