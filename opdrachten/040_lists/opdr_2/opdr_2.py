import os
if os.name == 'nt': os.system('cls')

'''# Student info 
# Opdracht 040_lists - opdr 1
# Naam student: Jordy Brink
# Groep:4ITX7 
'''

rivier_info = {"rijn": ["nederland", "duitsland", "Frankrijk"], "maas": ["nederland", "belgië", "duitsland"],"nijl": ["egypte", "soedan", "oeganda"]}
rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Opdracht 1: Print de 1e rivier en het 2e land waar de rivier doorheen stroomt
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")

# Opdracht 2: Print de 2e rivier en het 1e land waar de 2e rivier doorheen stroomt
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[1]][0].capitalize()}")

# Opdracht 3: Print de 3e rivier en het 3e land waar de rivier doorheen stroomt
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[2]][2].capitalize()}")
