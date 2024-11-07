# Opdracht 080_4
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
def vraag_feestgangers():
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"]
    feestgangers = []
    while True:
        antwoorden = {}
        for i, vraag in enumerate(vragen, start=1):
            antwoord = input(f"{i}. {vraag}\n")
            antwoorden[vragen[i-1]] = antwoord
        feestgangers.append(antwoorden)
        meer_feestgangers = input("Wil je nog iemand toevoegen? (ja/nee): ").lower()
        if meer_feestgangers != 'ja':
            break
    with open("PARTYYY.txt", "a") as bestand:
        for feestganger in feestgangers:
            bestand.write("----\n")
            for key, value in feestganger.items():
                bestand.write(f"{key}: {value}\n")
    print("Bedankt voor het invullen!")
    print("See you at the party.")
vraag_feestgangers()
