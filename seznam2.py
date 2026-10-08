def spocitej_prumer(student):
    if not student["znamky"]:
        print("v seznamu nejsou zadne prvky")
        return None
    prumer = sum(student["znamky"]) / len(student["znamky"])
    return round(prumer, 1)

def formatuj_text(student):
    prumer = spocitej_prumer(student)
    if prumer is None:
        return f"Student {student['jmeno']} {student['prijmeni']} nema zadne znamky."
    return f"Student {student['jmeno']} {student['prijmeni']} ma prumer: {prumer:.2f}"

if __name__ == "__main__":

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 23,
        "znamky": [3, 2, 1, 3, 2, 3]
    }

    print(formatuj_text(student))
    