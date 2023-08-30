from random import randint




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
    return tajemka


print(secret_code())
