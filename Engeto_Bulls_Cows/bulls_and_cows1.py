import os
from random import randint, seed


oddelovac = '-' * 48   


def secret_code():
    ''' generate random int as as secret code'''
    return str(randint(2000, 9999))


def ask_user_for_code():
    ''' získání vstupu od uživatele'''
    one_number = input('Hádej 4 znakový kód:')
    return one_number

def ziskej_indexy_pismen(slovo, hadani):
    indexy = []
    for index, symbol in enumerate(slovo):
        if symbol in hadani:
            indexy.append(index)
    return indexy


### hra ##################################################################
def game():
    code = secret_code()
    print(code)
    game_is_running  = True

    pocet = 0

    while game_is_running:

        bulls = 0
        cows = 0
      
              
        hadani = ask_user_for_code()
        print(f"Tajny cod je: {code}")
        print(f"Uzivatel zadal: {hadani}")   

        pocet += 1

        if hadani == code:
            print("Uhádl jsi, gratuluji.")    
            game_is_running = False   
        else:
            game_is_running = True

            i = 0
            for char_hadani in hadani:  
                
                #print(char_hadani)
                indexy = ziskej_indexy_pismen(code, char_hadani)
                
                #print(indexy)
                #print(i)
                #print(f" stav {bulls} bulls, {cows} cows") 
                if len(indexy) == 0:
                    break
                elif i in indexy:   
                    bulls += 1
                else:
                    cows += 1    

                     
                i += 1    

            print(f"{bulls} bulls, {cows} cows") 
            print(oddelovac)

    print(f"Correct, you've guessed the right number \n in {pocet} guesses!")

               

game()
