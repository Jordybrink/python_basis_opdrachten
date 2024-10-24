'''# Student info 
# Opdracht 090 - opdr 1
# Naam student: Jordy Brink
# Groep:4ITX7 
'''
import math

def kubus_vol(zijde):
    """Bereken het volume van een kubus."""
    return zijde ** 3  # Volume van een kubus = zijde^3

# Voorbeeld gebruik
volume_kubus = kubus_vol(5)
print(f"De inhoud van deze kubus is: {volume_kubus}")

###

def bol_vol(straal):
    """Bereken het volume van een bol."""
    return (4/3) * math.pi * (straal ** 3)  # Volume van een bol = (4/3) * pi * straal^3

# Voorbeeld gebruik
volume_bol = bol_vol(4)
print(f"De inhoud van deze bol is: {volume_bol}")

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))