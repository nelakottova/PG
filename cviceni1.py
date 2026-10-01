def add(a, b):
    c = a + b
    return c

def mul(a, b, c):
    vysledek = a * b * c
    return vysledek

def div(a, b):
    if b == 0:
        return "Nelze dělit nulou!"
    else:
        return a / b

def je_delitelne_beze_zbytku(a, b):
    if a%b == 0:
        return "je delitelne beze zbytku"
    else:
        return "neni delitelne beze zbytku"

def je_delitelne_3(a):
    if je_delitelne_beze_zbytku (a, 3) == "je delitelne beze zbytku":
        return "je delitelne 3"
    else:
        return "neni delitelne 3"

if __name__ == "__main__":
    x = add(5, 10)
    y = mul(2, 3, 4)
    z = div(10, 2)
    w = je_delitelne_beze_zbytku(10, 2) 
    v = je_delitelne_3(10)
    print(x) 
    print(y)
    print(z)
    print(w)    
    print(v)


