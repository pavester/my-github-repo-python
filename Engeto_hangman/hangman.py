# TODO importy zakladnich knihoven (modulu) - zabudovaných knihoven
import random

# import název knohovny importuj metodu
from pprint import pprint

# TODO importy vlastnich modulu
import slova
import grafika


#pprint(slova.hadana_slova)
# TODO promenne
zivoty = 7
hra_bezi = True
#random.seed(1)
slovo = random.choice(slova.hadana_slova)
tajemka = ['_'] * len(slovo)


# TODO hlavni smycka hry
while hra_bezi and zivoty >= 0:
    print(" ".join(tajemka))
    print(slovo)
    print(zivoty)
    print(grafika.obesenec[7-zivoty])

      
    # TODO input
    hadani = input("Hadej pismeno / slovo:") 

    # TODO pokud uzivatel uhadl cele slovo

    if slovo == hadani:
        print("Uhadl jsi tajne slovo")
        hra_bezi = False
    elif hadani in slovo and len(hadani) == 1:
        # TODO pokud uzivatel uhadne pismeno
        for index, symbol in enumerate(slovo):

        if symbol == hadani:
            tajemka[index-1] = hadani


        print("Uhadl jsi pismenko:")
    else:
        # TODO pokud uzivatel uhadl spatne pismeno
        print("Pismeno je špatně")
        zivoty -= 1
else:
    if not hra_bezi:
         print("Vyhrál jsi")  
    else:      
        print("Prohrál jsi")  
    
   



# TODO vypis else po tom, co je while cyklus prerusen