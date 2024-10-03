# Student info 
# Opdracht 040_lists - opdr 1
# Naam student: Jordy Brink
# Groep:4ITX7 
""" Opdracht voorbeeld 
    mylist = ...
    dict_1 = ...
    dict_2 = ...
    dict_3 = ...
    dict_4 = ...
    { "id": 0, "voornaam": "", "achternaam": "" }
"""

mylist = []
dict_1 = { "id": 0, "voornaam": "John", "achternaam": "Doe" }
dict_2 = { "id": 1, "voornaam": "Jane", "achternaam": "Smith" }
dict_3 = { "id": 2, "voornaam": "Alice", "achternaam": "Johnson" }
dict_4 = { "id": 3, "voornaam": "Bob", "achternaam": "Brown" }

mylist.extend([dict_1, dict_2, dict_3, dict_4])

print(mylist[0]["voornaam"], mylist[0]["achternaam"])
print(mylist[1]["voornaam"], mylist[1]["achternaam"])
print(mylist[2]["voornaam"], mylist[2]["achternaam"])
print(mylist[3]["voornaam"], mylist[3]["achternaam"])