list = (
    "koupelna",
    "zona",
    "syr",
    "teta",
    "kriz",
    "rodina",
    "nacitani",
    "cokolada",
    "asociace",
    "lavicka",
    "povrch",
    "rotace",
    "zamestnanec",
    "balicek",
    "komunikace",
    "popularni",
    "veta"
    ,"auto"
    )


def vytvor_soubor():
    ''' zalozi soubor '''
    i=0

    with open("slova.txt", mode="w", encoding="utf-8") as f:
        for hodnota in list:
            f.write(list[i])
            f.write("\n")
            i+=1




def zobraz_slova(soubor : str) -> list:
    ''' zobrazuje soubor '''

    vystup = []
    
    with open("slova.txt", mode="r") as f:
        for radek in  f.readlines():
            #print(str(radek))
            #radek = radek.strip("\n")

            print(radek, len(radek))
            if len(radek) >= 7:
                vystup.append(radek)
    
    return vystup


if __name__== "__main__":
    vytvor_soubor()
    print(zobraz_slova("slova.txt"))

