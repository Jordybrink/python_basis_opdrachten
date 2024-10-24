import os

def clearscreen():
    os.system("cls")

huidig_pad = os.path.abspath(__file__)
pad_delen = huidig_pad.split(os.sep)
pad = os.path.join(pad_delen[-3], pad_delen[-2], pad_delen[-1])

me = "Jordy Brink, 9710460, Groep: 4ITX7\n"

clearscreen()

print(me,pad)
print()