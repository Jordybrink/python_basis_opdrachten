import os

def cls():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
cls()

def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344

def miles_naar_kilometers(miles):
    return miles * 1.609344

kilometers = 200
miles = 500

miles_converted = kilometers_naar_miles(kilometers)
km_converted = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_converted} miles")
print(f"{miles} miles = {km_converted} kilometers")
