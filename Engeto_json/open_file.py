import os

#pathlib
soubory = os.listdir()

print(type(soubory))

for soubor in soubory:
    s = os.path.join(os.getcwd(),"soubor.txt")
    s = s.split(os.sep)
    print(s)

