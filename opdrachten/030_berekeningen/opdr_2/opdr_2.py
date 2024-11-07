# Opdracht 030_2
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

input_temperatuur = input("Voer een temperatuur in (zoals: 10c of 20f): ")
temperatuur = float(input_temperatuur[:-1])
unit = input_temperatuur[-1].lower()
if unit == "c":
    fahrenheit = (temperatuur * 9 / 5) + 32
    print(f"{temperatuur} graden Celsius is gelijk aan {fahrenheit} graden Fahrenheit.")
elif unit == "f":
    celsius = (temperatuur - 32) * 5 / 9
    print(f"{temperatuur} graden Fahrenheit is gelijk aan {celsius} graden Celsius.")
else:
    print("Ongeldige invoer. Gebruik 'c' voor Celsius of 'f' voor Fahrenheit.")
