# Opdracht
# Student: Jordy Brink
# St.nummer: 98104602
# Groep:4ITX7

# Lijst met pizza's
pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizza_lijst.sort()
print(pizza_lijst)

# Voeg een pizza naar keuze toe
pizza_lijst.append('Beast')
print(pizza_lijst)

# Verwijder de pizza die je het minst lekker vindt (bijvoorbeeld 'olivio')
pizza_lijst.remove('olivio')
print(pizza_lijst)

# Print de eerste 3 pizza's uit de lijst
print(pizza_lijst[:3])

# Print alleen de middelste pizza uit de lijst
# Aangezien de lijst 5 elementen heeft, is de middelste pizza de 3e in de lijst
print([pizza_lijst[len(pizza_lijst) // 2]])

# Print de laatste 3 pizza's uit de lijst
print(pizza_lijst[-3:])
