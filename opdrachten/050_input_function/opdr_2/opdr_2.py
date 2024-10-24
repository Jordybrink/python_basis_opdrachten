
gasten = ["Jordy", "Paul", "Kees", "Marie", "Hilda"]

print("Lijst met gasten:", gasten)
gasten.remove("Marie")

print("Marie heeft afgezegd:", gasten)
index_van_kees = gasten.index("Kees")
gasten.insert(index_van_kees + 1, "George")

print(f"George wil ook mee: {gasten}")
print()