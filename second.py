
def cislo_text(cislo): # Funkce, která převede číslo na text
    cisla = {
        0: "nula",
        1: "jedna",
        2: "dva",
        3: "tři",
        4: "čtyři",
        5: "pět",
        6: "šest",
        7: "sedm",
        8: "osm",
        9: "devět",
        10: "deset",
        11: "jedenáct",
        12: "dvanáct",
        13: "třináct",
        14: "čtrnáct",
        15: "patnáct",
        16: "šestnáct",
        17: "sedmnáct",
        18: "osmnáct",
        19: "devatenáct",
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát",
        100: "sto"
    }

    cislo = int(cislo) # int() převede vstup na celé číslo

    if cislo in cisla:
        return cisla[cislo]

    if 21 <= cislo <= 99:
        desitky = (cislo // 10) * 10 # Získání desítek např 25//10 = 2, 2*10 = 20 -> Program už ví, že potřebuje slovo „dvacet“
        jednotky = cislo % 10 # Získání jednotek 25 % 10 = 5 -> Program už ví, že potřebuje slovo „pět“
        return cisla[desitky] + " " + cisla[jednotky] # + spojí text dohromady, " " mezera mezi slovy

    return "Číslo není podporováno"


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: ")) # Získání vstupu od uživatele a převedení na celé číslo
    print(cislo_text(cislo))

