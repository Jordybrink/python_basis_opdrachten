# Opdracht 090_1
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

def write_to_file(file_name, text):
    """Schrijft tekst naar een bestand. Als het bestand al bestaat, wordt de tekst toegevoegd."""
    with open(file_name, 'a') as file:  # 'a' staat voor append, dus voeg toe aan het bestand
        file.write(text + '\n')  # Voeg een nieuwe regel toe na de tekst

# Voorbeeld van het gebruik van de functie
my_tekst = ("dikke bmw")
my_file = "LOG.txt"
write_to_file(my_file, my_tekst)

exit()