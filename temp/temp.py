def prevedCisloNaZnak(cislo):
 
    if (cislo >= 0 and cislo <= 9):
        return chr(48 + cislo)
    else:
        return chr(65 - 10 + cislo)


def PrevodCisel(zadaneCislo, soustava): 
    #tocim dokud je co delit
    vysledek =""
    pocet_cyklu = 1

    while (zadaneCislo > 0): 
        #print(zadaneCislo)
        vysledek += prevedCisloNaZnak(zadaneCislo % soustava)
        zadaneCislo = int(zadaneCislo / soustava)    
        pocet_cyklu +=1

        if pocet_cyklu > 5:
            break

    return vysledek


def nacti_Vstup(co_nacitam, hlaska_pro_uzivatele):
    spatne = True
    while spatne:

        if co_nacitam == "cislo":
            try:
                cislo= int(input(hlaska_pro_uzivatele))
                if cislo < 0: 
                    print("Zadané číslo musí být nezáporné!\n")
                    spatne = False
                    continue                  
            except ValueError:
                print(text_chyba)
        else:
       
    return nacteneCislo 


#Funkce nacte od uivatele číslo soustavy, na kterou che převést. 
#Načtené číslo musí být kladný integer.
def nactiBazi(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            nactenaBaze = int(input(text_zadani))
            if nactenaBaze < 0: 
              print("Zadané číslo musí být nezáporné!\n")
              continue
            if nactenaBaze < 2 or nactenaBaze > 16:
              print("Zadané číslo musí v rozmezí 2-16!\n")
              continue  
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return nactenaBaze 

# Hlavní program
zadaneCislo = nactiCislo();
baze = nactiBazi("Číselná soustava (2-16): ", "Neplatné zadání!\n");
print("Číslo ve zvolené soustavě:", fromDeci(vysledek, baze, zadaneCislo));