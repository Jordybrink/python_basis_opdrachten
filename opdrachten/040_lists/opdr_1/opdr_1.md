# Python basis

### Lists
Deze opdracht hoort bij de cursus python op [edutorial.nl](https://www.edutorial.nl/course/python)

### Opdracht

* Maak gebruik van het bestand: opdr_1.py
* Pas de code aan van opdr_1.py
* Commit en push je code naar github of bewaar in onedrive

Schrijf een programma waarin je een list aanmaakt.
Daarnaast maak je 4 dictionaries om gegevens van personen in op te slaan. Je mag zelf namen bedenken.
```python
{ "id": 0, "voornaam": "", "achternaam": "" }
```
Voeg de 4 dictionaries toe aan de list. Maak hierbij gebruik van een list-methode
Print de volledige naam van de 2e persoon op het scherm door de juiste gegevens op de plek van de vraagtekens te zetten.

> print(lijst[?][?], lijst[?][?])

### chat GPT code
    # Maak een lege lijst aan
    personen = []

    # Maak 4 dictionaries aan met gegevens van personen
    persoon_1 = { "id": 0, "voornaam": "John", "achternaam": "Doe" }
    persoon_2 = { "id": 1, "voornaam": "Jane", "achternaam": "Smith" }
    persoon_3 = { "id": 2, "voornaam": "Alice", "achternaam": "Johnson" }
    persoon_4 = { "id": 3, "voornaam": "Bob", "achternaam": "Brown" }

    # Voeg de dictionaries toe aan de lijst met een list-methode
    personen.extend([persoon_1, persoon_2, persoon_3, persoon_4])

    # Print de volledige naam van de 2e persoon
    print(personen[1]["voornaam"], personen[1]["achternaam"])