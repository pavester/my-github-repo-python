velikost = 10
symboly = ['#',' ']
sachovnice = []
# Iteruj přes řádky šachovnice a vytvoř proměnnou "rada"
for radek in range(velikost):
    rada = []
    # Iteruj přes jednotlivé buňky v každém řádku
    for bunka in range(velikost):
        # Vytvoř index, který vybere jednu z hodnot v proměnné "symboly"
        index = (radek + bunka) % len(symboly)
        rada.append(symboly[index])
    # Přidej hotové buňky do proměnné "sachovnice"
    sachovnice.append(''.join(rada))
# Vypiš výslednou šachovnici
print('\n'.join(sachovnice))