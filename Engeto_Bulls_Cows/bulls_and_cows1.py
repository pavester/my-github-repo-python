"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie

author: Pavel Štěrba
email: pavel.sterba@hotmail.com
discord: pavelsterba99
"""

import os
from random import randint, seed


separator = '-' * 48   

def print_header():
    ''' ptint user welcome'''
    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)



def generate_secret_code():
    ''' generate random int as as secret code until code is 4 digits length'''
    
    generate_is_running = True
    generate_code = ""

    while generate_is_running:

        one_suggested_digit = str(randint(1,9))
        
        if one_suggested_digit not in generate_code:
            generate_code += one_suggested_digit
        #print(tajemka)

        if len(generate_code) == 4:
            generate_is_running = False    

        #print(losuj)
    #print(f"Tajny code je: {generate_code}")    
    return generate_code
#####################################################################

def ask_user_for_code():
    ''' take input rfom user and validete that user provided valid code'''
    
    imput_validation = True

    while imput_validation:
    
        user_guess = input('Enter a number:')

        
        if len(user_guess) !=4:
            print("The number must have exactly 4 digits. Wrong attempt, guess again.")
            imput_validation = True
        elif not user_guess.isdigit():
             print("The number is not numeric. Wrong attempt, guess again.")
             imput_validation = True   
        elif '0' == user_guess[0]:
             print("The number starts with zero. Wrong attempt, guess again.")
             imput_validation = True
        elif len(user_guess) != len(set(user_guess)):   
            print("The number contains duplicity. Wrong attempt, guess again.")
        else:
           imput_validation = False 

    return user_guess

#####################################################################

def get_letter_indexes(secret_code, what_char_search):
    ''' returm list of indexes where searching char occurs'''    
    indexy = []
    for index, symbol in enumerate(secret_code):
        if symbol in what_char_search:
            indexy.append(index)
    return indexy


def game_evaluation(score):
    
    if score == 1:
        rating = "mission impossible"
    elif score < 6:
        rating = "amazing"
    elif score < 11:
        rating = "average"
    else:
        rating = "not so good"

    print(f"Correct, you've guessed the right number \nin {score} {('guess' if score <=1 else 'guesses')}!")
    print(separator)
    print(f"That is {rating}.")       
    print(separator)

### hra ##################################################################
def game():
    ''' main funcion that does the game'''        
    secret_code = generate_secret_code()
    #print(code)
    game_is_running  = True

    score = 0 # how many turn user wull have

    while game_is_running:

        bulls = 0
        cows = 0
                   
        user_input = ask_user_for_code()
        
        score += 1

        if user_input == secret_code:
            # user have guesed correctly, terminate program
            game_is_running = False   
        else:
            game_is_running = True

            i = -1  # I will increse even for the first turn
            for one_user_char in user_input:  
                
                i += 1  
                #print(char_hadani)
                indexy = get_letter_indexes(secret_code, one_user_char)
                               
                if len(indexy) == 0:
                    continue
                elif i in indexy:   
                    bulls += 1
                else:
                    cows += 1        

            print(f">>> {bulls} {('bull' if bulls <=1 else 'bulls')}, {cows} {('cow' if cows <=1 else 'cows')}") 
            print(separator)
    return score



### final program ##################################################################              
print_header()
score = game()
game_evaluation(score)
