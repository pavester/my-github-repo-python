"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Pavel Sterba
email: pavel.sterba@hotmail.com
discord: pavelsterba99

"""

TEXTS1 = ["""Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""]

TEXTS2 = ["""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick."""]

TEXTS3 = ["""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""]

#import task_template.py # import ukaykového textu


registrovany_uzivatel = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

oddelovac = "-" * 40
txt = ""

jmeno = input("username:")
heslo = input("password:")

if( jmeno in registrovany_uzivatel.keys()):
    print(oddelovac)
    print("Welcome to the app, bob")    
    print("We have 3 texts to be analyzed.")        
    print(oddelovac)    
    volba = int(input("Enter a number btw. 1 and 3 to select: "))

    if volba  == 1:
        txt = " ".join(str(e) for e in TEXTS1)
    elif volba  == 2:
        txt = " ".join(str(e) for e in TEXTS2)
    elif volba  == 3:
        txt = " ".join(str(e) for e in TEXTS3)

#    print(txt)
#    print(type(txt))

    rozdeleny_text = txt.split()
#    print(rozdeleny_text)
#    print(len(rozdeleny_text))

# inicialiyace promenych
    slovo_title = 0
    slovo_uppercase = 0
    slovo_lowercase = 0
    slovo_numeric = 0    
    soucet = 0
    cetnost = {}


    for slovo in rozdeleny_text:
        if slovo.istitle():
           slovo_title = slovo_title + 1

        if slovo.isupper():
           slovo_uppercase = slovo_uppercase + 1

        if slovo.islower():
           slovo_lowercase = slovo_lowercase + 1

        if slovo.isdigit():
           slovo_numeric = slovo_numeric + 1
           soucet = soucet + int(slovo)

        delka = len(slovo)

        if  delka in cetnost.keys() > 0:
            cetnost[delka] = [cetnost[delka], 1]
        else:
            cetnost[delka] = 1      


    print(f"There are {len(rozdeleny_text)} words in the selected text.")
    print(f"There are {slovo_title} titlecase words.")
    print(f"There are {slovo_uppercase} uppercase words.")
    print(f"There are {slovo_lowercase} lowercase words.")
    print(f"There are {slovo_numeric} numeric strings.")
    print(f"The sum of all the numbers {soucet}")

    
else:
    print("unregistered user, terminating the program..")    

print(cetnost)

