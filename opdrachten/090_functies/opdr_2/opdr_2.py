'''# Student info 
# Opdracht 090 - opdr 1
# Naam student: Jordy Brink
# Groep:4ITX7 
'''

def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344
def miles_naar_kilometers(miles):
    return miles * 1.609344

miles_converted = kilometers_naar_miles(kilometers)
km_converted = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_converted} miles")
print(f"{miles} miles = {km_converted} kilometers")

# input
kilometers = 200
miles = 200
