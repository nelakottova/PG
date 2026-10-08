if __name__=="__main__":

    vek = input("zadej svuj vek: ")
    print(f"Tvuj vek je {vek}")

    vek = int(vek)

    if vek >= 21:
        print("Muzes pit v USA")
    else:
        print("Dej si kolu")

    print(f"za rok ti bude {vek + 1}")

    seznam = [1, 2, 3, "ctyri", 5]
    print(seznam)
    seznam.append("ahoj")  
    print(seznam[2])

    print(f"seznam ma {len(seznam)} prvku")
    