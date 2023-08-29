"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie

author: Pavel Štěrba
email: pavel.sterba@hotmail.com
discord: pavelsterba99
"""

import os
from random import randint, seed


oddelovac = '-' * 48   

def hlavicka():
    print("Hi there!")
    print(oddelovac)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(oddelovac)



def secret_code():
    ''' generate random int as as secret code'''
    
    losuj = True
    tajemka = ""

    while losuj:

        navrh = str(randint(1,9))
        
        if navrh not in tajemka:
            tajemka += navrh
        #print(tajemka)

        if len(tajemka) == 4:
            losuj = False    

        #print(losuj)
    print(f"Tajny cod je: {tajemka}")    
    return tajemka
#####################################################################

def ask_user_for_code():
    ''' získání vstupu od uživatele'''
    
    kvalita_kodu = True

    while kvalita_kodu:
    
        one_number = input('Enter a number:')

        
        if len(one_number) !=4:
            print("The number must have exactly 4 digits. Try again.")
            kvalita_kodu = True
        elif '0' == one_number[0]:
             print("The number starts with zero. Try again")
             kvalita_kodu = True
        elif len(one_number) != len(set(one_number)):   
            print("The number contains duplicity. Try again.")
        else:
           kvalita_kodu = False 

    return one_number

#####################################################################

def ziskej_indexy_pismen(slovo, hadani):
    indexy = []
    for index, symbol in enumerate(slovo):
        if symbol in hadani:
            indexy.append(index)
    return indexy


def vyhodnoceni(score):
        print(f"Correct, you've guessed the right number \nin {score} {('guess' if score <=1 else 'guesses')}!")

### hra ##################################################################
def game():
    code = secret_code()
    #print(code)
    game_is_running  = True

    score = 0 # how many turn user wull have

    while game_is_running:

        bulls = 0
        cows = 0
                   
        hadani = ask_user_for_code()
        
        score += 1

        if hadani == code:
            # user have guesed correctly, terminate program
            game_is_running = False   
        else:
            game_is_running = True

            i = -1  # I will increse even for the first turn
            for char_hadani in hadani:  
                
                i += 1  
                #print(char_hadani)
                indexy = ziskej_indexy_pismen(code, char_hadani)
                               
                if len(indexy) == 0:
                    continue
                elif i in indexy:   
                    bulls += 1
                else:
                    cows += 1        

            print(f">>> {bulls} {('bull' if bulls <=1 else 'bulls')}, {cows} {('cow' if cows <=1 else 'cows')}") 
            print(oddelovac)
    return score



### final program ##################################################################              
hlavicka()
score = game()
vyhodnoceni(score)
