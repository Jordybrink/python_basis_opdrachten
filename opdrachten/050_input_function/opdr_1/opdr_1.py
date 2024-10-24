"""# Student info 
# Opdracht 040_lists - opdr 1
# Naam student: Jordy Brink
# Groep:4ITX7 
"""

import os
import math

def clearscreen():
    os.system("cls")

def vraag_waarde(bericht):
    clearscreen()
    
# Vraag om de lengte van de eerste en tweede zijde
zijde1 = float(input("Geef de lengte van de eerste zijde: ").replace(',', '.'))
zijde2 = float(input("Geef de lengte van de tweede zijde: ").replace(',', '.'))

# Bereken de lengte van de schuine zijde met de stelling van Pythagoras
schuine_zijde = (zijde1**2 + zijde2**2)**0.5

# Rond het resultaat af op 2 decimalen
schuine_zijde = round(schuine_zijde, 2)

# Toon de lengte van de schuine zijde
print(f"De lengte van de schuine zijde is: {schuine_zijde}")
