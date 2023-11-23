import os


def najdi_vsechny_txt(cesta: str) -> list:
    '''vrátí list všech souborů na cestě cesta'''
    cesty = os.path.join(cesta, soubor) for soubor in os.listdir(cesta)
    return cesty


def nacti_txt(soubor: str) -> list:
    '''vrátí obsah souboru'''
    with open(soubor, mode="r", encoding="utf-8") as f:
        obsah = f.readline()
    print("zpracovavam soubor", soubor)    
    return obsah    


def zformatuj_data(obsah: list) -> list:
    return obsah


def uloz_vysledek(obsah: list, soubor: str):
    with open(soubor, mode="w", encoding="utf-8") as f:
        f.writelines(obsah)
    print("vysledek byl ulozen do souboru", soubor)



 def main():
    cesty = nacti_txt(cesta = "vstupy")
    print(cesty)

    for (i, cesta) in enumerate(cesty):
        soubor = nacti_txt(cesta)
        obsah = zformatuj_data(obsah)
        jmeno_souboru = f"vystup{i}.txt"
        vystup_cesta = os.path.join("vystupy", jmeno_souboru)
        uloz_vysledek(obsah, soubor= "vystupy")




if __name__ == "__main__":
   main()
