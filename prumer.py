def spocitej_prumer(seznam):
    if not seznam:
        print("v seznamu nejsou zadne prvky")
        return None
    return sum(seznam) / len(seznam)   

if __name__ == "__main__":
    seznam = [5, 2, 6, 4, 5]
    prumer = spocitej_prumer(seznam)
    print(f"Prumer seznamu {seznam} je: {prumer}")