import os

def cls():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
cls()

import math

def kubus_vol(zijde):
    return zijde ** 3

volume_kubus = kubus_vol(5)
print(f"De inhoud van deze kubus is: {volume_kubus}")

def bol_vol(straal):
    return (4/3) * math.pi * (straal ** 3)

volume_bol = bol_vol(4)
print(f"De inhoud van deze bol is: {volume_bol}")

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))
