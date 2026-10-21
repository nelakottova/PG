def je_prvocislo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def vrat_prvocisla(maximum):
    return [n for n in range(2, maximum + 1) if je_prvocislo(n)]
