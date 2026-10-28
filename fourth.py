def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.

    :param figurka: Slovník s klíči 'typ' a 'pozice' (např. {"typ": "král", "pozice": (4, 4)})
    :param cilova_pozice: N-tice (řádek, sloupec)
    :param obsazene_pozice: Množina obsazených pozic
    :return: True, pokud je tah možný, jinak False
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    rozdil_radku = abs(cilova_pozice[0] - aktualni_pozice[0])
    rozdil_sloupcu = abs(cilova_pozice[1] - aktualni_pozice[1])

    if typ == "král":
        if rozdil_radku <= 1 and rozdil_sloupcu <= 1:
            if rozdil_radku != 0 or rozdil_sloupcu != 0:
                return True

    elif typ == "jezdec":
        if (rozdil_radku == 2 and rozdil_sloupcu == 1) or (rozdil_radku == 1 and rozdil_sloupcu == 2):
            return True

    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice)) 
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice)) 
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice))
