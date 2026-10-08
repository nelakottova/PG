def vynasob_xty_prvek(seznam, x, nasobek):
    if x < 1 or x > len(seznam):
        print("Chyba: x je mimo rozsah seznamu")
        return seznam

    seznam[x - 1] *= nasobek
    return seznam   

if __name__ == "__main__":  
    seznam = vynasob_xty_prvek([1, 2, 3, 4, 5], 3, 10)
    print(seznam)

