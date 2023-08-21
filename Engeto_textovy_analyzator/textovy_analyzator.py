"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Pavel Sterba
email: pavel.sterba@hotmail.com
discord: pavelsterba
"""

# import ukazkového textu
from task_template import TEXTS

# uživatelé a hesla
registrovany_uzivatel = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# inicializace promenych
statistika_slov = {"slovo_title" :0, "slovo_uppercase" : 0, "slovo_lowercase" : 0, "slovo_numeric" : 0, "soucet" : 0}
text_volba = 0
delka_slova = 0
cetnost = {}
txt = ""
oddelovac = "-" * 40


jmeno = input("username:")
heslo = input("password:")

if( jmeno in registrovany_uzivatel.keys()):
    print(oddelovac)
    print("Welcome to the app, bob")    
    print("We have 3 texts to be analyzed.")        
    print(oddelovac)    
    volba = (input("Enter a number btw. 1 and 3 to select: "))

    if  not volba.isnumeric() or not int(volba) in range(1,4):
        print("You need to enter a NUMBER between 1-3.")    
        print("Terminating the program.")
        quit() # konec programu
    else:
        text_volba = int(volba)-1 # vber textu, v Listu jsou číslovány od 0'''
        rozdeleny_text =  TEXTS[text_volba].split()

        for slovo in rozdeleny_text:
            if slovo.istitle():
                statistika_slov["slovo_title"] += 1

            if slovo.isupper():
                statistika_slov["slovo_uppercase"] += 1

            if slovo.islower():
                statistika_slov["slovo_lowercase"] += 1    

            if slovo.isdigit():
                statistika_slov["slovo_numeric"] += 1                
                statistika_slov["soucet"] += int(slovo)                       

            delka_slova = len(slovo)

            if  delka_slova not in cetnost:
                cetnost[delka_slova] = 1      
            else:
                cetnost[delka_slova] += 1      


        print(f"There are {len(rozdeleny_text)} words in the selected text.")
        print(f"There are {statistika_slov['slovo_title']} titlecase words.")
        print(f"There are {statistika_slov['slovo_uppercase']} uppercase words.")
        print(f"There are {statistika_slov['slovo_lowercase']} lowercase words.")
        print(f"There are {statistika_slov['slovo_numeric']} numeric strings.")
        print(f"The sum of all the numbers {statistika_slov['soucet']}")

        # graf
        print(f'LEN|    OCCURENCES    |NR.')
        print(oddelovac)

        for key, value in sorted(cetnost.items()):
            if key <= 9:   
                print(f"{key}  {'*' * value } {' ' * (18-value) }| {value}")
            else:  
                print(f"{key}  {'*' * value } {' ' * (17-value) }| {value}")

        print(oddelovac)
        print("Have a nice day.")
        print(oddelovac)
        print()

else:
        print("unregistered user, terminating the program..")    