import csv

def schrijf_csv(bestandsnaam, data):
    with open(bestandsnaam, mode='w', newline='') as bestand:
        schrijver = csv.writer(bestand)
        for rij in data:
            schrijver.writerow(rij)